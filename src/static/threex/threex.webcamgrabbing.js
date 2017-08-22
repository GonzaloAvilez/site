var THREEx = THREEx || {}

// shim
navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;
window.URL = window.URL || window.webkitURL;

/**
 * Grab camera
 * @constructor
 */
THREEx.WebcamGrabbing = function(){

	//////////////////////////////////////////////////////////////////////////////////
	//		Comments
	//////////////////////////////////////////////////////////////////////////////////
        // create video element
        var domElement = document.createElement('video')
        var videoSelect = document.querySelector('select#videoSource');
        var selectors = [videoSelect];
        domElement.setAttribute('autoplay', true)

	// window.domElement = video
	domElement.style.zIndex = -1;
        domElement.style.position = 'absolute'

	// domElement.style.top = '50%'
	// domElement.style.left = '50%'
	// domElement.style.marginRight = '50%'
	// domElement.style.transform = 'translate(-50%, -50%)'
	// domElement.style.minWidth = '100%'

	domElement.style.top = '0px'
	domElement.style.left = '0px'
	domElement.style.width = '100%'
	domElement.style.height = '100%'

        /**
         * Resize video element.
         * - Made complex to handle the aspect change
         * - it is frequently when the mobile is changing orientation
         * - after a search on the internet, it seems hard/impossible to prevent browser from changing orientation
         */
        function onResize(){
                // is the size of the video available ?
                if( domElement.videoHeight === 0 )   return

                var videoAspect = domElement.videoWidth / domElement.videoHeight
                var windowAspect = window.innerWidth / window.innerHeight

                // var video = document.querySelector('video')
//                 if( videoAspect < windowAspect ){
//                         domElement.style.left        = '0%'
//                         domElement.style.width       = window.innerWidth + 'px'
//                         domElement.style.marginLeft  = '0px'
//
//                         domElement.style.top         = '50%'
//                         domElement.style.height      =  (window.innerWidth/videoAspect) + 'px'
//                         domElement.style.marginTop   = -(window.innerWidth/videoAspect) /2 + 'px'
// console.log('videoAspect <<<<< windowAspect')
//                 }else{
//                         domElement.style.top         = '0%'
//                         domElement.style.height      = window.innerHeight+'px'
//                         domElement.style.marginTop   =  '0px'
//
//                         domElement.style.left        = '50%'
//                         domElement.style.width       =  (window.innerHeight*videoAspect) + 'px'
//                         domElement.style.marginLeft  = -(window.innerHeight*videoAspect)/2 + 'px'
// console.log('videoAspect >>>> windowAspect')
//                 }
        }

        window.addEventListener('resize', function(event){
                onResize()
        })

        // just to be sure - resize on mobile is funky to say the least
        setInterval(function(){
                onResize()
        }, 500)

        //Before times version for three.js

        // function gotSources(sourceInfos) {
        //   for (var i = 0; i !== sourceInfos.length; ++i) {
        //     var sourceInfo = sourceInfos[i];

        //     var option = document.createElement('option');
        //     option.value = sourceInfo.deviceId;

        //     if (sourceInfo.kind === 'videoinput') {
        //       option.text = sourceInfo.label || 'camera ' + (videoSelect.length + 1);
        //       videoSelect.appendChild(option);
        //     } else {
        //       console.log('Some other kind of source: ', sourceInfo);
        //     }
        //   }
        // }
        // if (typeof MediaStreamTrack === 'undefined' ||
        //     typeof MediaStreamTrack.getSources === 'undefined') {
        //   alert('This browser does not support MediaStreamTrack.getSources().');
        // } else {
        //   navigator.mediaDevices.enumerateDevices().then(function(e){
        //     gotSources(e)
        //   });
        // }

        // function successCallback(stream) {
        //   window.stream = stream; // make stream available to console
        //   domElement.src = window.URL.createObjectURL(stream);
        //   domElement.play();
        // }

        // function errorCallback(error) {
        //   console.log('navigator.getUserMedia error: ', error);
        // }

        // function start() {
        //   if (window.stream) {
        //     domElement.src = null;
        //     window.stream.getTracks().forEach(function(track){
        //       track.stop();
        //     })
        //   }
        //   var videoSource = videoSelect.value;

        //   var constraints = {
        //     video: {
        //       optional: [{
        //         sourceId: videoSource
        //       }]
        //     }
        //   };
        //   navigator.getUserMedia(constraints, successCallback, errorCallback);
        // }

        // videoSelect.onchange = start;
        // start();



        function gotDevices(deviceInfos) {
          // Handles being called several times to update labels. Preserve values.
          var values = selectors.map(function(select) {
            return select.value;
          });
          selectors.forEach(function(select) {
            while (select.firstChild) {
              select.removeChild(select.firstChild);
            }
          });
          for (var i = 0; i !== deviceInfos.length; ++i) {
            var deviceInfo = deviceInfos[i];
            var option = document.createElement('option');
            option.value = deviceInfo.deviceId;
            if (deviceInfo.kind === 'videoinput') {
              option.text = deviceInfo.label || 'camera ' + (videoSelect.length + 1);
              videoSelect.appendChild(option);
            } else {
              console.log('Some other kind of source/device: ', deviceInfo);
            }
          }
          selectors.forEach(function(select, selectorIndex) {
            if (Array.prototype.slice.call(select.childNodes).some(function(n) {
              return n.value === values[selectorIndex];
            })) {
              select.value = values[selectorIndex];
            }
          });
        }

        navigator.mediaDevices.enumerateDevices().then(gotDevices).catch(handleError);



        function gotStream(stream) {
          window.stream = stream; // make stream available to console
          					domElement.srcObject = stream;
          // Refresh button list in case labels have become available
          return navigator.mediaDevices.enumerateDevices();
        }

        function start() {
          if (window.stream) {
            window.stream.getTracks().forEach(function(track) {
              track.stop();
            });
          }
          var videoSource = videoSelect.value;
          var constraints = {
            video: {deviceId: videoSource ? {exact: videoSource} : undefined}
          };
          navigator.mediaDevices.getUserMedia(constraints).
              then(gotStream).then(gotDevices).catch(handleError);
        }

        videoSelect.onchange = start;

        start();

        function handleError(error) {
          console.log('navigator.getUserMedia error: ', error);
        }






        // // get the media sources
        // MediaStreamTrack.getSources(function(sourceInfos) {
        //         // define getUserMedia() constraints
        //         var constraints = {
        //                 video: true,
        //                 audio: false,
        //         }
        //         // to mirror the video element when it isnt 'environment'
        //         // domElement.style.transform   = 'scaleX(-1)'

        //         // it it finds the videoSource 'environment', modify constraints.video
        //         for (var i = 0; i != sourceInfos.length; ++i) {
        //                 var sourceInfo = sourceInfos[i];
        //                 if(sourceInfo.kind == "video" && sourceInfo.facing == "environment") {
        //                         constraints.video = {
        //                                 optional: [{sourceId: sourceInfo.id}]
        //                         }
        //                         // not to mirror the video element when it is 'environment'
        //                         // domElement.style.transform   = ''
        //                 }
        //         }

        //         // try to get user media
        //         navigator.getUserMedia( constraints, function(stream){
        //                 domElement.src = URL.createObjectURL(stream);
        //         }, function(error) {
        //                 console.error("Cant getUserMedia()! due to ", error);
        //         });
        // });

	this.domElement = domElement
}






          
		  function CustomFeatures(){
            var texture_to_Reflect = new THREE.TextureLoader().load( texture_to_Reflect_path ); 
                texture_to_Reflect.mapping = THREE.SphericalReflectionMapping;
            var materials_acerina = new THREE.MeshStandardMaterial( {
                                        color :0xbfbfbf,                       
                                        emissive : 0xbc1a1a,
                                        emissiveIntensity : 0.06,
                                        roughness : 0.36,
                                        metalness: 0.89,
                                        envMap : texture_to_Reflect,                       
                                        map : texture_map,
                                        shading : THREE.SmoothShading,
                                        side : THREE.DoubleSide,
                                    } );
            var materials_volcanic = new THREE.MeshStandardMaterial( {
                                        color :0x989898,                       
                                        emissive : 0xbc1a1a,
                                        emissiveIntensity : 0.08,
                                        roughness : 0.34,
                                        metalness: 0.58,
                                        envMap : texture_to_Reflect,                       
                                        map : texture_map,
                                        shading : THREE.SmoothShading,
                                        side : THREE.DoubleSide,
                                    } );
            var materials_volcanic_base = new THREE.MeshStandardMaterial( {
                                        color :0x989898,                       
                                        emissive : 0xaf5c5c,
                                        emissiveIntensity : 0.08,
                                        roughness : 0.49,
                                        metalness: 0.6,
                                        envMap : texture_to_Reflect,                      
                                        map : texture_map,
                                        shading : THREE.SmoothShading,
                                        side : THREE.DoubleSide,
                                    } );

            var loader = new THREE.ObjectLoader();
             loader.load(loading_model3d,function ( object,materials ) {              
                    var beadings = object.getObjectByName("beading_head");
                    var bracelet1 = object.getObjectByName("beading_left");
                    var bracelet2 = object.getObjectByName("beading_central");
                    var bracelet3 = object.getObjectByName("beading_right");
                    var lion = object.getObjectByName("lion");
                    bracelet1.traverse(function (child) {
                        if (child instanceof THREE.Mesh) {
                            child.material = materials_acerina;
                        }
                    });
                    bracelet2.traverse(function (child) {
                        if (child instanceof THREE.Mesh) {
                            child.material = materials_volcanic_base;
                        }
                    });
                    bracelet3.traverse(function (child) {
                        if (child instanceof THREE.Mesh) {
                            child.material = materials_volcanic;
                        }
                    });
                    beadings.traverse(function (child) {
                        if (child instanceof THREE.Mesh) {
                            child.material = materials_acerina;
                        }
                    });
                    lion.traverse(function (child) {
                        if (child instanceof THREE.Mesh) {
                            child.material = materials_acerina;
                        }
                    });

                    scene.add( bracelet1 );
                        scene.add( bracelet2 );
                            scene.add( bracelet3 );
                                scene.add( beadings );
                                    scene.add( lion );       
                });
    }

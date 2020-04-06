    function CustomFeatures(){
          var texture_to_Reflect = new THREE.TextureLoader().load( texture_to_Reflect_path ); 
                texture_to_Reflect.mapping = THREE.SphericalReflectionMapping;
          var  silver_materials = new THREE.MeshStandardMaterial( {
                                            color : 0xffffff,                           
                                            emissive   : 0xbc1a1a,
                                            emissiveIntensity : 0.08,
                                            roughness : 0.18,
                                            metalness: 0.91,
                                            envMap     : texture_to_Reflect,
                                            map : texture_map,
                                            shading : THREE.SmoothShading,
                                            side : THREE.DoubleSide,
                                        } );
          var loader = new THREE.ObjectLoader();
            loader.load(loading_model3d,function ( object ) {
                        var leopardos = object.getObjectByName("leopard_head");
                        var pulsera = object.getObjectByName("bracelet");
                        pulsera.material.metalness = 0.0;
                        pulsera.material.roughness = 1.0;
                        pulsera.material.shininess = 0.0;
                        pulsera.material.bumpScale = 0.4;
                        leopardos.traverse(function(child) {     
                            if (child instanceof THREE.Mesh) {
                                child.material = silver_materials;
                                child.geometry.computeVertexNormals();
                            }
                        });            
                    scene.add(object);
                    scene.add(leopardos);
       
                });
    }
	
		
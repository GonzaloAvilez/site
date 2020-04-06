function CustomFeatures(){
       var texture_to_Reflect = new THREE.TextureLoader().load( texture_to_Reflect_path); 
        texture_to_Reflect.mapping = THREE.SphericalReflectionMapping;

            var parameters = {
                                color :0xffffff,                       
                                emissive : 0xffdada ,
                                emissiveIntensity : 0.293,
                                roughness : 0.2,
                                metalness: 1,
                                opacity: 1.00,
                                envMap : true,
                                smooth : true
                            }
        var front_materials = new THREE.MeshStandardMaterial({
                            color :0x2b2b2b,                      
                            emissive   : 0x595959,
                            opacity: 0.95,
                            emissiveIntensity : 0.0,
                            roughness : 0.26,
                            metalness: 1.0,
                            side : THREE.FrontSide, 
                            shading : THREE.SmoothShading, 
                            transparent: true,
                            envMap : texture_to_Reflect
                            })
        var back_materials = new THREE.MeshStandardMaterial({
                            color :0x2b2b2b,                      
                            emissive   : 0x595959,
                            opacity: 1.0,
                            emissiveIntensity : 0.0,
                            roughness : 0.06,
                            metalness: 0.91,
                            envMap : texture_to_Reflect,                         
                            side : THREE.BackSide,
                            shading : THREE.SmoothShading, 
                           
                            })
        var  materials_acerina = new THREE.MeshStandardMaterial( {
                                        color :0xbfbfbf,                       
                                        emissive : 0xbc1a1a,
                                        emissiveIntensity : 0.06,
                                        roughness : 0.36,
                                        metalness: 0.79,
                                        envMap : texture_to_Reflect,                       
                                        map : texture_map,
                                        shading : THREE.SmoothShading,
                                        side : THREE.DoubleSide,
                                    } );
        var  materials_onix = new THREE.MeshStandardMaterial( {
                                    color :0x919191,                       
                                    emissive : 0x494949,
                                    emissiveIntensity : 0.144,
                                    roughness : 0.23,
                                    metalness: 1.0,
                                    envMap : texture_to_Reflect,                       
                                    map : texture_map,
                                    shading : THREE.SmoothShading,
                                    side : THREE.DoubleSide,
                                    } );

        var metalMaterials = {
            'silver' :new THREE.MeshStandardMaterial( {
                                     color :0xffffff    ,                       
                                    emissive : 0xffdada ,
                                    emissiveIntensity : 0.293,
                                    roughness : 0.2,
                                    metalness: 1,
                                    envMap : texture_to_Reflect,                      
                                    map : texture_map,
                                    shading : THREE.SmoothShading,
                                    side : THREE.DoubleSide,
                                    } ),
            'gold': new THREE.MeshStandardMaterial( {
                                    color :0xe8c036,                      
                                    emissive : 0xef9935,
                                    emissiveIntensity : 0.31,
                                    roughness : 0.2,
                                    metalness: 1.0,
                                    envMap : texture_to_Reflect,                      
                                    map : texture_map,
                                    shading : THREE.SmoothShading,
                                    side : THREE.DoubleSide,
                                    } ),
            'black': new THREE.MeshStandardMaterial( {
                                   color :0x707070,                  
                                    emissive : 0xffdada,
                                    emissiveIntensity : 0.0,
                                    roughness : 0.2,
                                    metalness: 1.0,
                                    envMap : texture_to_Reflect,                      
                                    map : texture_map,
                                    shading : THREE.SmoothShading,
                                    side : THREE.DoubleSide,
                                    } ),
            }
    
            var loader = new THREE.ObjectLoader();
            loader.load(loading_model3d,function ( object ) {
                    var beadings = object.getObjectByName("beadings_central");
                    var bracelet = object.getObjectByName("beadings");         
                    var crown = object.getObjectByName("crown");
                    var gemstones = object.getObjectByName("zircon");
                    bracelet.traverse(function (child) {
                        if (child instanceof THREE.Mesh) {
                            child.material = materials_onix;
                        }
                    });
                    crown.traverse(function (child) {
                        if (child instanceof THREE.Mesh) {
                            child.material = metalMaterials.silver;
                                    $(document).ready(function() {
                                        $("input[type='button']").click(function() {
                                          switch(this.id) {
                                            case 'button_silver': 
                                            child.material = metalMaterials.silver; 
                                            break;
                                            case 'button_gold': 
                                            child.material = metalMaterials.gold; 
                                            break;
                                            case 'button_black': 
                                            child.material = metalMaterials.black; 
                                            break;
                                            default:
                                            child.material = metalMaterials.silver; 
                                          }
                                        });
                                    });
                            child.geometry.computeVertexNormals();
                        }
                    });
                    
                    beadings.traverse(function (child) {
                        if (child instanceof THREE.Mesh) {
                            child.material = metalMaterials.silver;
                            $(document).ready(function() {
                                        $("input[type='button']").click(function() {
                                          switch(this.id) {
                                            case 'button_silver': 
                                            child.material = metalMaterials.silver; 
                                            break;
                                            case 'button_gold': 
                                            child.material = metalMaterials.gold; 
                                            break;
                                            case 'button_black': 
                                            child.material = metalMaterials.black; 
                                            break;
                                            default:
                                            child.material = metalMaterials.silver; 
                                          }
                                        });
                                    });
                        }
                    });
      
                    gemstones.traverse(function(child) {     
                        if (child instanceof THREE.Mesh) {
                            child.material = back_materials;
                            var second_child = child.clone();
                            second_child.material = front_materials;
                            var parent = new THREE.Group();
                            parent.add(second_child);
                            parent.add(child);     
                            scene.add(parent);
                        }
                    });

                    scene.add( beadings );
                        scene.add( bracelet );
                            scene.add( crown );
                                scene.add( parent );
                                    scene.add( beadings );       
                });


    }
		
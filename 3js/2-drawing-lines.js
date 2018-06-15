const camera = new _3.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 1, 500);
camera.position.set(0, 0, 100);
camera.lookAt(new _3.Vector3(0, 0, 0));

const scene = new _3.Scene();

const material = new _3.LineBasicMaterial({ color: 0x0000ff });

const geometry = new _3.Geometry();
geometry.vertices.push(new _3.Vector3(-10, 0, 0));
geometry.vertices.push(new _3.Vector3(0, 10, 0));
geometry.vertices.push(new _3.Vector3(10, 0, 0));

const line = new _3.Line(geometry, material);

scene.add(line);
renderer.render(scene, camera);

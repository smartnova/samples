const scene = new _3.Scene();
const camera = new _3.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

const geometry = new _3.BoxGeometry(1, 1, 1);
const material = new _3.MeshBasicMaterial({ color: 0x00ff00 });
const cube = new _3.Mesh(geometry, material);
scene.add(cube);

camera.position.z = 5;

function animate() {
  requestAnimationFrame(animate);

  cube.rotation.x += 0.02;
  cube.rotation.y += 0.02;

  renderer.render(scene, camera);
}
animate();

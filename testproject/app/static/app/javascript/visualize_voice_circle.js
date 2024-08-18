const visualizer_container = document.querySelector('.visualizer-container');
let visualizer_audio_context;

const startVisualizer = () => {
    if (visualizer_audio_context) return;

    const num_points = 64;
    const point_radius = 100;

    visualizer_audio_context = new AudioContext();

    const analyser = visualizer_audio_context.createAnalyser();
    analyser.fftSize = 256;
    const bufferLength = analyser.frequencyBinCount;
    const dataArray = new Uint8Array(bufferLength);

    const points = [];

    for (let i = 0; i < num_points; i++) {
        const angle = (i / num_points) * 2 * Math.PI;
        const x = point_radius * Math.cos(angle);
        const y = point_radius * Math.sin(angle);

        const point = document.createElement('div');
        point.className = 'visual-point';
        point.style.position = 'absolute';
        point.style.top = `calc(50% + ${y}px)`;
        point.style.left = `calc(50% + ${x}px)`;
        visualizer_container.appendChild(point);

        points.push(point);
    };

    navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
        visualizer_audio_context.createMediaStreamSource(stream).connect(analyser);

        const loop = () => {
            window.requestAnimationFrame(loop);

            analyser.getByteFrequencyData(dataArray);

            for (let i = 0; i < num_points; i++) {
                const value = dataArray[Math.floor(i * (bufferLength / num_points))];
                points[i].style.transform = `scale(${1 + value / 100})`;
                points[i].style.background = `rgb(${value}, 0, 0)`;
            };
        };
        loop();

    }).catch(error => {
        console.error(error);
    });
    startVisualizer();
};

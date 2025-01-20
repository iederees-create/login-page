<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Matrix-like animation using JavaScript and HTML">
    <title>Matrix Effect</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            background-color: black;
            color: #00FF00;
            font-family: monospace;
            height: 100vh;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0;
            padding: 0;
        }
        canvas {
            display: block;
        }
        #overlayText {
            position: absolute;
            color: rgba(0, 255, 0, 1);
            font-size: 40px;
            font-family: monospace;
            z-index: 2;
            text-align: center;
            user-select: none;
        }
    </style>
</head>
<body>
    <canvas id="matrixCanvas"></canvas>
    <div id="overlayText">Welcome to NextGenWebs</div>
    <script>
        const canvas = document.getElementById('matrixCanvas');
        const ctx = canvas.getContext('2d');

        // Set canvas size
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        // Matrix effect settings
        const columns = Math.floor(canvas.width / 20); // Number of columns
        const drops = Array(columns).fill(0); // Array to store drop positions

        // Matrix character set
        const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()_+-=[]{}|;:,.<>?/~";

        // Function to draw matrix effect
        function draw() {
            // Clear screen with slight transparency
            ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // Set glowing green color
            ctx.fillStyle = 'rgba(0, 255, 0, 0.9)';  // Bright green with some transparency
            ctx.font = '20px monospace';

            // Loop through each drop in the matrix
            for (let i = 0; i < drops.length; i++) {
                const text = chars[Math.floor(Math.random() * chars.length)];  // Random character
                ctx.fillText(text, i * 20, drops[i] * 20);

                // Reset drop position after it moves past the screen height
                if (drops[i] * 20 > canvas.height && Math.random() > 0.975) {
                    drops[i] = 0;
                }

                // Move drop down
                drops[i]++;
            }
        }

        // Animation loop to update the matrix effect
        function update() {
            draw();
            requestAnimationFrame(update);
        }

        // Start the animation loop
        update();
    </script>
</body>
</html>
// Futuristic Ben 10 Omnitrix Custom Cursor & Particle Trail
document.addEventListener('DOMContentLoaded', () => {
    // Only initialize on devices with a fine pointer (mouse/trackpad) to disable on mobile
    if (window.matchMedia('(pointer: coarse)').matches) return;

    // Create DOM elements for the main cursor
    const cursor = document.createElement('div');
    cursor.id = 'omnitrix-cursor';
    cursor.className = 'omnitrix-cursor';

    const ring = document.createElement('div');
    ring.className = 'cursor-ring';

    const core = document.createElement('div');
    core.className = 'cursor-core';

    cursor.appendChild(ring);
    cursor.appendChild(core);
    document.body.appendChild(cursor);

    // Create Canvas for the particle trail
    const canvas = document.createElement('canvas');
    canvas.id = 'cursor-trail';
    document.body.appendChild(canvas);

    const ctx = canvas.getContext('2d');
    let width = window.innerWidth;
    let height = window.innerHeight;
    canvas.width = width;
    canvas.height = height;

    // Resize handler for canvas
    window.addEventListener('resize', () => {
        width = window.innerWidth;
        height = window.innerHeight;
        canvas.width = width;
        canvas.height = height;
    });

    // Tracking positions
    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    let cursorX = mouseX;
    let cursorY = mouseY;
    let isHovering = false;

    // Particles array for trail and sparks
    const particles = [];

    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;

        // Add particles on move to create a flowing energy trail
        addParticle(mouseX, mouseY);
        // Occasionally emit an extra spark
        if (Math.random() > 0.7) {
            addParticle(mouseX, mouseY, true);
        }
    });

    // Hover detection for interactive elements to pulse and expand
    const interactiveSelectors = 'a, button, input, select, .series-card, .season-pill, .episode-card, .btn-action, .btn-terabox, .btn-icon-action';

    const addHoverListeners = () => {
        document.querySelectorAll(interactiveSelectors).forEach(el => {
            if (el.dataset.hasCursorListener) return;
            el.dataset.hasCursorListener = "true";

            el.addEventListener('mouseenter', () => {
                isHovering = true;
                cursor.classList.add('active');
            });
            el.addEventListener('mouseleave', () => {
                isHovering = false;
                cursor.classList.remove('active');
            });
        });
    };

    addHoverListeners();
    const observer = new MutationObserver(() => {
        addHoverListeners();
    });
    observer.observe(document.body, { childList: true, subtree: true });

    function addParticle(x, y, isSpark = false) {
        const spread = isHovering ? 15 : 5;
        const offsetX = (Math.random() - 0.5) * spread;
        const offsetY = (Math.random() - 0.5) * spread;

        particles.push({
            x: x + offsetX,
            y: y + offsetY,
            size: isSpark ? Math.random() * 4 + 2 : Math.random() * 2 + 1,
            life: 1,
            velocity: {
                x: isSpark ? (Math.random() - 0.5) * 4 : (Math.random() - 0.5) * 1,
                y: isSpark ? (Math.random() - 0.5) * 4 - 1 : (Math.random() - 0.5) * 1 - 0.5
            },
            color: Math.random() > 0.5 ? '#00ff41' : '#00b02c'
        });
    }

    function animate() {
        cursorX += (mouseX - cursorX) * 0.15;
        cursorY += (mouseY - cursorY) * 0.15;
        cursor.style.transform = `translate(${cursorX}px, ${cursorY}px)`;

        ctx.clearRect(0, 0, width, height);

        for (let i = particles.length - 1; i >= 0; i--) {
            const p = particles[i];

            p.x += p.velocity.x;
            p.y += p.velocity.y;
            p.life -= Math.random() * 0.03 + 0.01; 

            if (p.life <= 0) {
                particles.splice(i, 1);
                continue;
            }

            ctx.beginPath();
            ctx.arc(p.x, p.y, p.size * p.life, 0, Math.PI * 2);

            ctx.fillStyle = p.color;
            ctx.globalAlpha = p.life;
            ctx.shadowBlur = 8;
            ctx.shadowColor = p.color;
            ctx.fill();
        }

        ctx.globalAlpha = 1;
        ctx.shadowBlur = 0;

        requestAnimationFrame(animate);
    }

    animate();
});

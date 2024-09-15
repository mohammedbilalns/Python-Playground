window.onload = function() {
    const canvas = document.createElement('canvas');
    canvas.style.position = 'fixed';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.zIndex = '-1';
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    document.body.appendChild(canvas);
  
    const ctx = canvas.getContext('2d');
  
    const circles = [];
    const polygons = [];
    const symbols = [];
  
    function createCircle() {
      const radius = Math.random() * 5 + 2; // Random radius between 2 and 7
      const x = Math.random() * canvas.width;
      const y = Math.random() * canvas.height;
      const dx = (Math.random() - 0.5) * 2; // Random horizontal speed
      const dy = (Math.random() - 0.5) * 2; // Random vertical speed
  
      return { radius, x, y, dx, dy };
    }
  
    function createPolygon() {
      const numSides = Math.floor(Math.random() * 5) + 3; // Random number of sides between 3 and 7
      const radius = Math.random() * 10 + 5; // Random radius between 5 and 15
      const x = Math.random() * canvas.width;
      const y = Math.random() * canvas.height;
      const dx = (Math.random() - 0.5) * 2; // Random horizontal speed
      const dy = (Math.random() - 0.5) * 2; // Random vertical speed
  
      return { numSides, radius, x, y, dx, dy };
    }
  
    function createSymbol() {
      const symbols = ['π', 'e', '∞', '√', '∫', '∑'];
      const symbol = symbols[Math.floor(Math.random() * symbols.length)];
      const fontSize = Math.random() * 20 + 10; // Random font size between 10 and 30
      const x = Math.random() * canvas.width;
      const y = Math.random() * canvas.height;
      const dx = (Math.random() - 0.5) * 2; // Random horizontal speed
      const dy = (Math.random() - 0.5) * 2; // Random vertical speed
  
      return { symbol, fontSize, x, y, dx, dy };
    }
  
    for (let i = 0; i < 20; i++) { // Create 50 circles, polygons, and symbols initially
      circles.push(createCircle());
      polygons.push(createPolygon());
      symbols.push(createSymbol());
    }
  
    function drawCircles() {
      for (const circle of circles) {
        ctx.beginPath();
        ctx.arc(circle.x, circle.y, circle.radius, 0, 2 * Math.PI);
        ctx.fillStyle = 'white'; // Set the fill color to white
        ctx.fill();
        ctx.strokeStyle = 'black'; // Set the stroke color to black
        ctx.stroke(); // Draw the black border
  
        circle.x += circle.dx;
        circle.y += circle.dy;
  
        // Bounce off the walls
        if (circle.x - circle.radius < 0 || circle.x + circle.radius > canvas.width) {
          circle.dx = -circle.dx;
        }
        if (circle.y - circle.radius < 0 || circle.y + circle.radius > canvas.height) {
          circle.dy = -circle.dy;
        }
      }
    }
  
    function drawPolygons() {
      for (const polygon of polygons) {
        ctx.beginPath();
        ctx.moveTo(polygon.x + polygon.radius * Math.cos(0), polygon.y + polygon.radius * Math.sin(0));
  
        for (let i = 1; i <= polygon.numSides; i++) {
          const angle = (i * 2 * Math.PI) / polygon.numSides;
          ctx.lineTo(polygon.x + polygon.radius * Math.cos(angle), polygon.y + polygon.radius * Math.sin(angle));
        }
  
        ctx.closePath();
        ctx.fillStyle = 'white'; // Set the fill color to white
        ctx.fill();
        ctx.strokeStyle = 'black'; // Set the stroke color to black
        ctx.stroke(); // Draw the black border
  
        polygon.x += polygon.dx;
        polygon.y += polygon.dy;
  
        // Bounce off the walls
        if (polygon.x - polygon.radius < 0 || polygon.x + polygon.radius > canvas.width) {
          polygon.dx = -polygon.dx;
        }
        if (polygon.y - polygon.radius < 0 || polygon.y + polygon.radius > canvas.height) {
          polygon.dy = -polygon.dy;
        }
      }
    }
  
    function drawSymbols() {
      for (const symbol of symbols) {
        ctx.font = `${symbol.fontSize}px Arial`;
        ctx.fillStyle = 'black'; // Set the fill color to black
        ctx.fillText(symbol.symbol, symbol.x, symbol.y);
  
        symbol.x += symbol.dx;
        symbol.y += symbol.dy;
  
        // Bounce off the walls
        if (symbol.x < 0 || symbol.x > canvas.width) {
          symbol.dx = -symbol.dx;
        }
        if (symbol.y < 0 || symbol.y > canvas.height) {
          symbol.dy = -symbol.dy;
        }
      }
    }
  
    function drawObjects() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      drawCircles();
      drawPolygons();
      drawSymbols();
      requestAnimationFrame(drawObjects);
    }
  
    drawObjects();
  };
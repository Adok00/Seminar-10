<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Modern Coffee Shop</title>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Roboto&display=swap" rel="stylesheet">
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Roboto', sans-serif;
      background: #fdfcfb;
      color: #333;
      scroll-behavior: smooth;
    }
    header {
      background: url('https://images.unsplash.com/photo-1509042239860-f550ce710b93') no-repeat center center/cover;
      height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      color: white;
      text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
      animation: fadeIn 2s ease-in;
    }
    @keyframes fadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }
    header h1 {
      font-family: 'Playfair Display', serif;
      font-size: 4rem;
      animation: slideInDown 1s ease-out;
    }
    @keyframes slideInDown {
      from { transform: translateY(-50px); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }
    header p {
      font-size: 1.5rem;
      animation: slideInUp 1s ease-out;
    }
    @keyframes slideInUp {
      from { transform: translateY(50px); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }
    nav {
      background-color: #333;
      display: flex;
      justify-content: center;
      position: sticky;
      top: 0;
      z-index: 1000;
    }
    nav a {
      color: white;
      padding: 1rem;
      text-decoration: none;
      font-weight: bold;
      transition: background 0.3s;
    }
    nav a:hover {
      background: #555;
    }
    section {
      padding: 60px 20px;
      max-width: 1200px;
      margin: auto;
      animation: fadeIn 1s ease-in;
    }
    .section-title {
      font-family: 'Playfair Display', serif;
      font-size: 2.5rem;
      margin-bottom: 20px;
      text-align: center;
    }
    .menu, .gallery, .testimonials, .contact {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 20px;
    }
    .card {
      background: white;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
      overflow: hidden;
      transition: transform 0.3s;
    }
    .card:hover {
      transform: translateY(-5px);
    }
    .card img {
      width: 100%;
      height: 200px;
      object-fit: cover;
    }
    .card-content {
      padding: 15px;
    }
    .testimonial {
      font-style: italic;
    }
    footer {
      background: #333;
      color: white;
      text-align: center;
      padding: 20px;
    }
    .cta {
      background: #6f4e37;
      color: white;
      text-align: center;
      padding: 40px 20px;
      animation: fadeIn 1s ease-in;
    }
    .cta h2 {
      font-size: 2rem;
    }
    .cta button {
      padding: 10px 20px;
      background: white;
      color: #6f4e37;
      border: none;
      margin-top: 20px;
      cursor: pointer;
      font-weight: bold;
    }
    .cta button:hover {
      background: #ddd;
    }
    iframe {
      width: 100%;
      height: 400px;
      border: none;
      border-radius: 10px;
    }
    .gallery {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }

    .gallery-item img {
      width: 100%;
      height: 180px;
      object-fit: cover;
      border-radius: 10px;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
      transition: transform 0.3s ease;
    }

    .gallery-item img:hover {
      transform: scale(1.03);
    }

    .modal {
      display: none;
      position: fixed;
      z-index: 2000;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      overflow: auto;
      background: rgba(0, 0, 0, 0.5);
}

    .modal-content {
      background: #fff;
      margin: 10% auto;
      padding: 30px;
      border-radius: 10px;
      width: 80%;
      max-width: 400px;
      text-align: center;
      box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

    .close {
      color: #aaa;
      float: right;
      font-size: 24px;
      font-weight: bold;
      cursor: pointer;
}

    .close:hover {
      color: #333;
}

    .btn-directions {
      display: inline-block;
      margin-top: 20px;
      padding: 10px 20px;
      background-color: #4CAF50;
      color: white;
      text-decoration: none;
      border-radius: 5px;
      font-size: 16px;
}

    .btn-directions:hover {
      background-color: #45a049;
}


  </style>
</head>

<script>
  function openModal() {
    document.getElementById('modal').style.display = 'block';
  }

  function closeModal() {
    document.getElementById('modal').style.display = 'none';
  }

  window.onclick = function(event) {
    const modal = document.getElementById('modal');
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }
</script>

<body>
  <header>
    <h1>Velvet Coffee</h1>
    <p>Where every cup tells a story</p>
  </header>

  <nav>
    <a href="#about">About</a>
    <a href="#menu">Menu</a>
    <a href="#gallery">Gallery</a>
    <a href="#testimonials">Testimonials</a>
    <a href="#contact">Contact</a>
  </nav>

  <section id="about">
    <h2 class="section-title">About Us</h2>
    <p style="text-align:center; max-width:700px; margin:auto;">Velvet Coffee is a cozy artisan coffee shop offering rich flavors, hand-crafted beverages, and a peaceful atmosphere perfect for work or relaxation.</p>
  </section>

  <section id="menu">
    <h2 class="section-title">Our Menu</h2>
    <div class="menu">
      <div class="card">
        <img src="https://avatars.mds.yandex.net/get-altay/11522875/2a0000018e4aecea635f3a3b3c44a527ef0b/XXL_height" alt="Espresso">
        <div class="card-content">
          <h3>Espresso</h3>
          <p>Strong and bold classic shot of espresso.</p>
        </div>
      </div>
      <div class="card">
        <img src="https://almode.club/uploads/posts/2023-12/thumbs/1701595966_almode-top-p-tekhniki-latte-arta-64.jpg" alt="Latte">
        <div class="card-content">
          <h3>Latte</h3>
          <p>Smooth milk with a perfect espresso base.</p>
        </div>
      </div>
      <div class="card">
        <img src="https://www.xpatathens.com/media/k2/items/cache/f0e832f2aa0cf1edd0fde90ad354cf32_M.jpg" alt="Mocha">
        <div class="card-content">
          <h3>Mocha</h3>
          <p>Chocolate-infused delight with whipped cream.</p>
        </div>
      </div>
    </div>
  </section>

 <section id="gallery">
  <h2 class="section-title">Gallery</h2>
  <div class="gallery">
    <div class="gallery-item">
      <img src="https://i.pinimg.com/736x/9b/3f/30/9b3f3062ec7531479ac130a4d5afd62f.jpg" alt="Интерьер кофейни">
    </div>
    <div class="gallery-item">
      <img src="https://img.championat.com/i/o/t/16405298911310757037.jpg" alt="Кофе на столе">
    </div>
    <div class="gallery-item">
      <img src="https://i.pinimg.com/originals/0e/bd/59/0ebd59690911d41945916ef7d04f21cb.jpg" alt="Бариста за работой">
    </div>
  </div>
</section>

  <section id="testimonials">
    <h2 class="section-title">Testimonials</h2>
    <div class="testimonials">
      <div class="card">
        <div class="card-content">
          <p class="testimonial">“Best coffee in town! Always fresh and delicious.”</p>
          <p>- Sarah M.</p>
        </div>
      </div>
      <div class="card">
        <div class="card-content">
          <p class="testimonial">“The atmosphere is perfect for studying or meeting friends.”</p>
          <p>- James R.</p>
        </div>
      </div>
      <div class="card">
        <div class="card-content">
          <p class="testimonial">“Their mocha is heavenly. Highly recommend!”</p>
          <p>- Emily T.</p>
        </div>
      </div>
    </div>
  </section>

 <section class="cta">
  <h2>Visit Us Today!</h2>
  <p>We are open every day from 8 AM to 8 PM.</p>
  <button onclick="openModal()">Get Directions</button>
</section>

<!-- Modal -->
<div id="modal" class="modal">
  <div class="modal-content">
    <span class="close" onclick="closeModal()">&times;</span>
    <h3>Thanks for your interest!</h3>
    <p>See you soon at Velvet Coffee!</p>
    <a href="https://www.google.com/maps" target="_blank" class="btn-directions">Get Directions</a>
  </div>
</div>

 <section id="contact">
  <h2 class="section-title">Contact Us</h2>
  <div class="contact">
    <div class="card">
      <div class="card-content">
        <h3>Address</h3>
        <p>пр. Сатпаева 123, Атырау, Казахстан</p>
      </div>
    </div>
    <div class="card">
      <div class="card-content">
        <h3>Email</h3>
        <p>info@velvetcoffee.kz</p>
      </div>
    </div>
    <div class="card">
      <div class="card-content">
        <h3>Phone</h3>
        <p>+7 7122 45 67 89</p>
      </div>
    </div>
  </div>
  <br>
  <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d95802.07643213448!2d51.8305065!3d47.0944956!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x41c939e176e8c4f3%3A0x6761c7aa3e2f2c45!2z0JDQtNC80LDRgtC40L3QsCwg0JDQstGC0L7Qu9C40Y8!5e0!3m2!1sru!2skz!4v1714827352192!5m2!1sru!2skz" allowfullscreen></iframe>
</section>

  <footer>
    <p>&copy; 2025 Velvet Coffee. All Rights Reserved.</p>
  </footer>
</body>
</html>

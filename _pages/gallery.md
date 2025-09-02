---
layout: page
title: Photo Gallery
permalink: /gallery/
subtitle: A collection of photos and memories
---

<div class="gallery-page">
  <div class="row">
    <div class="col-sm mt-3 mt-md-0">
      {% include figure.liquid path="assets/img/theronincar.jpeg" class="img-fluid rounded z-depth-1" title="Theron in his car" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
      {% include figure.liquid path="assets/img/IMG_7578.jpg" class="img-fluid rounded z-depth-1" title="Profile photo" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
      {% include figure.liquid path="assets/img/yellowstone.png" class="img-fluid rounded z-depth-1" title="Yellowstone National Park" %}
    </div>
  </div>
  
  <div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
      {% include figure.liquid path="assets/img/prof_pic_color.png" class="img-fluid rounded z-depth-1" title="Professional headshot" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
      {% include figure.liquid path="assets/img/1.jpg" class="img-fluid rounded z-depth-1" title="Sample image 1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
      {% include figure.liquid path="assets/img/2.jpg" class="img-fluid rounded z-depth-1" title="Sample image 2" %}
    </div>
  </div>
  
  <div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
      {% include figure.liquid path="assets/img/3.jpg" class="img-fluid rounded z-depth-1" title="Sample image 3" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
      {% include figure.liquid path="assets/img/4.jpg" class="img-fluid rounded z-depth-1" title="Sample image 4" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
      {% include figure.liquid path="assets/img/5.jpg" class="img-fluid rounded z-depth-1" title="Sample image 5" %}
    </div>
  </div>
  
  <div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
      {% include figure.liquid path="assets/img/6.jpg" class="img-fluid rounded z-depth-1" title="Sample image 6" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
      {% include figure.liquid path="assets/img/7.jpg" class="img-fluid rounded z-depth-1" title="Sample image 7" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
      {% include figure.liquid path="assets/img/8.jpg" class="img-fluid rounded z-depth-1" title="Sample image 8" %}
    </div>
  </div>
  
  <div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
      {% include figure.liquid path="assets/img/9.jpg" class="img-fluid rounded z-depth-1" title="Sample image 9" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
      {% include figure.liquid path="assets/img/10.jpg" class="img-fluid rounded z-depth-1" title="Sample image 10" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
      {% include figure.liquid path="assets/img/11.jpg" class="img-fluid rounded z-depth-1" title="Sample image 11" %}
    </div>
  </div>
  
  <div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
      {% include figure.liquid path="assets/img/12.jpg" class="img-fluid rounded z-depth-1" title="Sample image 12" %}
    </div>
  </div>
</div>

<style>
  .gallery-page {
    margin-top: 2rem;
  }
  
  .gallery-page .row {
    margin-bottom: 1rem;
  }
  
  .gallery-page img {
    transition: transform 0.3s ease;
  }
  
  .gallery-page img:hover {
    transform: scale(1.05);
  }
</style>

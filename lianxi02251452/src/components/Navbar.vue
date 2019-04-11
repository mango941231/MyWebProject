<template>
  <div class="header">
    <div class="content white">
      <nav class="navbar navbar-default">
        <div class="container">
          <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
              <span class="sr-only">Toggle navigation</span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="index.html">
              <h1>
                <!--<span class="fa fa-leanpub" aria-hidden="true"></span>Best Study-->
                <!--<label>Education & Courses</label>-->
                这个学校
              </h1>
            </a>
          </div>
          <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <nav class="link-effect-2" id="link-effect-2">
              <ul class="nav navbar-nav">
                <li class="active">
                  <a href="index.html" class="effect-3">首页</a>
                </li>
                <li>
                  <a href="about.html" class="effect-3">About Us</a>
                </li>
                <li>
                  <a href="courses.html" class="effect-3">Courses</a>
                </li>
                <li>
                  <a href="join.html" class="effect-3">Join Us</a>
                </li>
                <li class="dropdown">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown">Pages
                    <span class="caret"></span>
                  </a>
                  <ul class="dropdown-menu" role="menu">
                    <li>
                      <a href="icons.html">Web Icons</a>
                    </li>
                    <li>
                      <a href="codes.html">Short Codes</a>
                    </li>
                  </ul>
                </li>
                <li>
                  <a href="Gallery.html" class="effect-3">Gallery</a>
                </li>
                <li>
                  <a href="contact.html" class="effect-3">Contact Us</a>
                </li>
              </ul>
            </nav>
          </div>
        </div>
      </nav>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style scoped>

</style>

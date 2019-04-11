<template>
  <nav class="navbar navbar-expand-lg navbar-light" style="background-color: #e3f2fd;">
    <!--<a class="navbar-brand" href="#">Navbar</a>-->
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent" style="background-color: white">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <a class="nav-link" href="#">学校概况<span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">处室设置</a>
        </li>
        <li class="nav-item dropdown active" id="dropdownn">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            教育教学
          </a>
          <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <a class="dropdown-item" href="#">师资队伍</a>
            <a class="dropdown-item" href="#">学生工作</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="#">学生教育</a>
          </div>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">德育建设</a>
        </li>
      </ul>
      <!--<form class="form-inline my-2 my-lg-0">-->
        <!--<input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">-->
        <!--<button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>-->
      <!--</form>-->
    </div>
  </nav>
</template>

<script>
// import $ from 'jquery'
export default {
  name: 'NavMenu'
}
</script>

<style scoped>
  .dropdown:hover>.dropdown-menu {
    display: block;
  }
  .dropdown>.dropdown-toggle:active {
    pointer-events: none;
  }
</style>

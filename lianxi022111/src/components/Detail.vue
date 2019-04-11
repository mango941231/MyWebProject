<template>
  <div class="container-fluid" id="containerfluid">
    <div class="icon-list">
      <div class="row" id="iconlist-row">
        <div class="col-sm" id="iconlist-colsm-left">
          <a class="icon"><i class="fa fa-envelope-o fa-2x" aria-hidden="true"></i></a>
          <a class="icon"><i class="fa fa-user-circle fa-2x" aria-hidden="true"></i></a>
          <a class="icon"><i class="fa fa-bell fa-2x" aria-hidden="true"></i></a>
          <a class="icon"><i class="fa fa-coffee fa-2x" aria-hidden="true"></i></a>
        </div>
        <div class="col-sm" id="iconlist-colsm-right">
          <a class="icon"><i class="fa fa-modx fa-2x" aria-hidden="true"></i></a>
          <a class="icon"><i class="fa fa-optin-monster fa-2x" aria-hidden="true"></i></a>
          <a class="icon"><i class="fa fa-weibo fa-2x" aria-hidden="true"></i></a>
          <a class="icon"><i class="fa fa-facebook-official fa-2x" aria-hidden="true"></i></a>
        </div>
      </div>
    </div>
    <div class="container-fluid" id="bottomdetail">
      <div class="bottom-detail" id="newslist">
        <div class="row" id="bottomdetail-row">
          <div class="col-md-auto" id="bottomdetail-left">
            <img src="../../static/images/ujnlogo.png"></div>
          <div class="col-sm" id="bottomdetail-right">
            <p class="bottomdetail-text">市北校区地址:青岛市抚顺路11号   邮编:266033     长江路校区地址：青岛经济技术开发区长江中路2号 邮编：266520</p>
            <p class="bottomdetail-text">嘉陵江路校区地址:青岛经济技术开发区嘉陵江路777号   邮编:266520     临沂校区地址:临沂市费县县城东外环1号    邮编:273400</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Detail'
}
</script>

<style scoped>
#containerfluid{
  float: left;
  background-color: aqua;
  height: auto;
}
.bottom-detail{
  height: 80px;
  background-color: blueviolet;
}
#bottomdetail-left{
  float: left;
  width: 226px;
}
#bottomdetail-right{
  float: right;
  padding-top: 1%;
}
.bottomdetail-text{
  font-size: 10px;
}
.icon-list{
  text-align: center;
  height: 100px;
  padding-top: 2%;
}
#iconlist-colsm-left{
}
#iconlist-colsm-right{
  background-color: antiquewhite;
}
.icon{
  padding: 40px;
}
</style>

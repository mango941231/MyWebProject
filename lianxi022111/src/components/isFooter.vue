<template>
  <div class="container-fluid" id="containerfluid">
    <div class="icon-list">
      <div class="row" id="iconlist-row">
        <div class="col-sm" id="iconlist-colsm">
          <a class="icon"><i class="fa fa-envelope-o fa-2x" aria-hidden="true"></i>邮箱</a>
          <a class="icon"><i class="fa fa-user-circle fa-2x" aria-hidden="true"></i></a>
          <a class="icon"><i class="fa fa-bell fa-2x" aria-hidden="true"></i></a>
          <a class="icon"><i class="fa fa-coffee fa-2x" aria-hidden="true"></i></a>
          <a class="icon"><i class="fa fa-modx fa-2x" aria-hidden="true"></i></a>
          <a class="icon"><i class="fa fa-optin-monster fa-2x" aria-hidden="true"></i></a>
          <a class="icon"><i class="fa fa-weibo fa-2x" aria-hidden="true"></i></a>
          <a class="icon"><i class="fa fa-facebook-official fa-2x" aria-hidden="true"></i></a>
        </div>
      </div>
    </div>
    <div class="footer">
      <p>市北校区地址:青岛市抚顺路11号   邮编:266033     长江路校区地址：青岛经济技术开发区长江中路2号 邮编：266520</p>
      <p>嘉陵江路校区地址:青岛经济技术开发区嘉陵江路777号   邮编:266520     临沂校区地址:临沂市费县县城东外环1号    邮编:273400</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'isFooter'
}
</script>

<style scoped>
  .footer {
    /*position: absolute;*/
    bottom: 0;
    width: 100%;
    /* Set the fixed height of the footer here */
    height: 80px;
    background-color: #f5f5f5;
    float: left;
  }
  #containerfluid{
    float: left;
    background-color: aqua;
    height: auto;
    padding: 0px;
  }
  .icon-list{
    height: 250px;
    padding-top: 100px;
    text-align: center;
  }
  .icon{
    padding: 40px;
  }
  #iconlist-row{
    background-color: #eeeeee;
  }
</style>

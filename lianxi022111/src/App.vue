<template>
  <div id="app">
    <navmenu />
    <banner />
    <jznews />
    <isfooter />
  </div>
</template>

<script>
import NavMenu from '@/components/NavMenu'
import Banner from '@/components/Banner'
import JzNews from '@/components/JzNews'
import isFooter from '@/components/isFooter'
export default {
  name: 'app',
  components: {
    'navmenu': NavMenu,
    'banner': Banner,
    'jznews': JzNews,
    'isfooter': isFooter
  }
}
</script>

<style>
 body{
   margin: 0px;
   padding: 0px;
   border: 0px;
 }
</style>

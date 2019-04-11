<template>
  <div id="app" class="container-fluid">
  <navbar />
    <banner />
  </div>
</template>

<script>
import Navbar from '@/components/Navbar'
import Banner from '@/components/Banner'
export default {
  name: 'App',
  components: {
    'navbar': Navbar,
    'banner': Banner
  }
}
</script>

<style>
  body{
    margin: 0;
    padding: 0;
    border: 0;
  }
</style>

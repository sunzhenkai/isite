<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  created: function () {
    this.$store.dispatch('actionFetchCategories')
    if (!this.$store.getters.userInfo && this.isLogin) {
      this.$store.dispatch('actionGetUserInfo')
    }
  },
  computed: {
    isLogin: {
      get () {
        return this.$store.getters.token && this.$store.getters.token.length > 10
      }
    }
  }
}
</script>

<style>
</style>

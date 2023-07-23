<style lang="scss" scoped>
</style>

<template>
  <el-container>
    <el-header>
      <header-bar/>
      <login-register-modal/>
    </el-header>
    <el-main id="appMain">
        <app-main/>
    </el-main>
  </el-container>
</template>

<script>
import AppMain from './components/AppMain'
import HeaderBar from './components/HeaderBar'
import LoginRegisterModal from '@/views/components/modals/LoginRegisterModal'

export default {
  name: 'LayoutView',
  components: {
    AppMain,
    HeaderBar,
    LoginRegisterModal
  }
}
</script>

<style lang="scss" scoped>
</style>

<template>
  <el-menu :default-active="activeIndex" collapse-transition class="el-menu-demo" mode="horizontal" style="display: flex; justify-content: center;">
    <el-menu-item href="/" @click="$router.push({path: '/'})" class="nav-bar-menu-item brand m-x-5" style="border: none !important; position: absolute; left: 0;"><img src="/static/img/logo.png" style="width: 1.8rem;"></el-menu-item>
    <el-menu-item
      @click="$router.push({path: '/article/list/'})" :index="Math.random().toString()">文章</el-menu-item>
    <template v-for="(item, index) in categoryOptions">
      <el-submenu :index="(Date.now() + Math.random()).toString() + '1'" v-if="item.children && item.children.length > 0">
        <template slot="title">{{item.name}}</template>
        <el-menu-item
          @click="$router.push({path: '/article/list/?cate=' + encodeURIComponent(subItem.name)})"
          v-for="(subItem, idx) in item.children" :key="Math.random()" :index="Math.random().toString()">{{subItem.name}}</el-menu-item>
      </el-submenu>
      <el-menu-item
        @click="$router.push({path: '/article/list/?cate=' + encodeURIComponent(item.name)})"
        :index="(Date.now() + Math.random()).toString() + '2'" v-else>{{item.name}}</el-menu-item>
    </template>

    <el-menu-item  style="position: absolute; right: 0; border: none !important;">
      <div class="user-info-wrp" v-if="!isLogin">
        <el-button @click="showLoginModal" plain class="none-border">登录</el-button>
        <el-button @click="showRegisterModal">注册</el-button>
      </div>
      <div class="user-info-wrp" v-else>
        <el-popover
          placement="bottom"
          width="100"
          v-model="userInfoPopVisible"
          trigger="click">
          <div class="popover-menu">
            <a class="popover-menu-item m-y-1" href="javascript: void(0)" @click="onWriteArticleClick">写文章</a>
            <a class="popover-menu-item m-y-1" href="javascript: void(0)" @click="logout">退出</a>
          </div>
          <el-button plain class="none-border" slot="reference">{{userInfo ? userInfo.username : ''}}</el-button>
        </el-popover>
      </div>
    </el-menu-item>
  </el-menu>
</template>

<script>
  export default {
    name: 'HeaderComponent',
    data: function () {
      return {
        userInfoPopVisible: false,
        activeMenuItem: 0,
        activeIndex: '1',
      }
    },
    computed: {
      isLogin: {
        get () {
          return this.$store.getters.token && this.$store.getters.token.length > 10
        }
      },
      userInfo: {
        get () {
          if (this.isLogin) {
            return this.$store.getters.userInfo
          } else {
            return null
          }
        }
      },
      categoryOptions () {
        return this.$store.getters.categories
      }
    },
    methods: {
      showLoginModal: function () {
        this.$store.dispatch('actionShowLoginRegisterModal', {actionIsLogin: true})
      },
      showRegisterModal: function () {
        this.$store.dispatch('actionShowLoginRegisterModal', {actionIsLogin: false})
      },
      logout: function () {
        this.userInfoPopVisible = false
        this.$store.dispatch('actionLogout')
      },
      onWriteArticleClick: function () {
        this.userInfoPopVisible = false
        this.$router.push({name: 'writeArticle'})
      }
    }
  }
</script>

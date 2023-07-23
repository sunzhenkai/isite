<style lang="scss" scoped>
.el-header {
    height: 53px !important;
}
.el-menu-item {
    height: 53px !important;
    line-height: 53px !important;
}
.brand {
  border-bottom: none !important;
  margin-top: .1rem;
  margin-right: 1rem;
}
</style>

<template>
  <div v-if="false" class="nav-bar">
    <a href="javascript: void(0)" @click="onMenuItemClick(1)" class="nav-bar-menu-item brand"><img src="/static/img/logo.png" style="width: 1.8rem;"></a>
    <a href="javascript: void(0)" @click="onMenuItemClick(cate.name)"
       :class="['nav-bar-menu-item', (activeMenuItem === cate.name ? 'menu-item-active' : null)]"
       v-for="(cate, index) in categoryOptions"
       :key="Math.random()">{{cate.name}}</a>

    <!--    <a href="javascript: void(0)" @click="onMenuItemClick(2)" :class="['nav-bar-menu-item', (activeMenuItem === 2 ? 'menu-item-active' : null)]">文章</a>-->
    <a href="javascript: void(0)" @click="onMenuItemClick('我')" :class="['nav-bar-menu-item', (activeMenuItem === '我' ? 'menu-item-active' : null)]">我</a>
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
      <!--<el-button plain class="none-border">{{userInfo ? userInfo.username : ''}}</el-button>-->
    </div>
  </div>
</template>

<script>
export default {
  name: 'HeaderComponent',
  data: function () {
    return {
      userInfoPopVisible: false,
      activeMenuItem: 0
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
    categoryOptions() {
      return this.$store.getters.categories;
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
      this.userInfoPopVisible = false;
      this.$store.dispatch('actionLogout')
    },
    onWriteArticleClick: function () {
      this.userInfoPopVisible = false;
      this.$router.push({name: 'writeArticle'});
    },
    onMenuItemClick: function (key) {
      this.activeMenuItem = key;
      switch (parseInt(key)) {
        case 1:
          this.$router.push({name: 'index'});
          break;
        case 2:
          this.$router.push({name: 'articleList'});
          break;
        case 3:
          break;
      }
    }
  }
}
</script>

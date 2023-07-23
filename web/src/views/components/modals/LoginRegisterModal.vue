<style scoped>
.el-input__icon {
  width: 16px;
  margin: 0 8px;
}

.el-button {
  width: 100%;
}

.el-form {
  padding: 0 25px !important;
}
</style>

<template>
  <el-dialog
    :visible="modalVisible"
    @close="closeModal"
    width="450px"
    title="登录 / 注册">
    <el-form>
      <el-form-item>
        <el-input v-model="username">
          <icon slot="suffix" class="el-input__icon" name="user"/>
        </el-input>
      </el-form-item>
      <el-form-item>
        <el-input v-model="password" type="password">
          <icon slot="suffix" class="el-input__icon" name="lock"/>
        </el-input>
        <a href="javascript: void(0)" @click="actionIsLogin = !actionIsLogin"
           style="margin-top: 50px;">{{ actionIsLogin ? '还没有账号？点击注册' : '已有账号？点击登录' }}</a>
      </el-form-item>
      <el-button @click="actionLoginOrRegister">{{ actionIsLogin ? '登录' : '注册' }}</el-button>
    </el-form>
  </el-dialog>
</template>

<script>
import {Message} from 'element-ui'

export default {
  name: 'LoginRegisterModal',
  data: function () {
    return {
      username: '',
      password: ''
    }
  },
  computed: {
    actionIsLogin: {
      get: function () {
        return this.$store.getters.getActionIsLogin
      },
      set: function (flag) {
        this.$store.dispatch('actionSetActionIsLogin', {actionIsLogin: flag})
      }
    },
    modalVisible: {
      get () {
        return this.$store.state.UserStore.loginRegisterModalVisible
      }
    }
  },
  methods: {
    closeModal: function () {
      this.$store.dispatch('actionHideLoginRegisterModal')
    },
    actionLoginOrRegister: function () {
      let data = {
        username: this.username,
        password: this.password
      }
      if (this.actionIsLogin) {
        this.$store.dispatch('actionObtainToken', {data: data}).then(_ => {
          this.closeModal()
          Message({
            message: '登录成功!',
            type: 'success',
            duration: 1000
          })
        }).catch(error => {
          console.log(error)
        })
      } else {
        this.$store.dispatch('actionUserRegister', {data: data}).then(_ => {
          this.closeModal()
          Message({
            message: '注册成功!',
            type: 'success',
            duration: 1000
          })
        })
      }
    }
  }
}
</script>

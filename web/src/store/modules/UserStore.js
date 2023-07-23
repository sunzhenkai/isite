import userApi from '@/api/UserApi'
import {Message} from 'element-ui'
import cookie, {TOKEN_KEY} from '@/utils/cookie'

const state = {
  userInfo: null,
  token: cookie.getCookie(TOKEN_KEY),
  loginRegisterModalVisible: false,
  actionIsLogin: true
}

const getters = {
  userInfo: (state) => {
    return state.userInfo
  },
  token: (state) => {
    return state.token
  },
  getLoginRegisterModalVisible: (state) => {
    return state.loginRegisterModalVisible
  },
  getActionIsLogin: (state) => {
    return state.actionIsLogin
  },
  isLogin (state) {
    return state.userInfo != null
  }
}

const actions = {
  actionObtainToken: ({commit}, {data}) => {
    return new Promise(function (resolve, reject) {
      userApi.obtainToken(data).then(res => {
        commit('setToken', res.token)
        commit('setUserInfo', res.user)
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  actionSetLoginRegisterModalVisible: ({commit, state}, flag) => {
    commit('setLoginRegisterModalVisible', flag)
  },

  actionHideLoginRegisterModal: ({commit}) => {
    commit('setLoginRegisterModalVisible', false)
  },

  actionShowLoginRegisterModal: ({commit}, {actionIsLogin}) => {
    commit('setLoginRegisterModalVisible', true)
    commit('setActionIsLogin', actionIsLogin)
  },

  actionSetActionIsLogin: ({commit}, {actionIsLogin}) => {
    commit('setActionIsLogin', actionIsLogin)
  },

  actionUserRegister: ({commit, dispatch}, {data}) => {
    userApi.register(data).then(res => {
      commit('setUserInfo', res)
      dispatch('actionObtainToken', {data: data})
      return Promise.resolve()
    }).catch(error => {
      Message({
        message: error,
        type: 'error',
        duration: 3000
      })
      return Promise.reject(error)
    })
  },

  actionGetUserInfo: ({commit}) => {
    userApi.obtainUserInfo().then(res => {
      commit('setUserInfo', res)
    }).catch(error => {
      console.log('error: ' + error)
      Message({
        message: '获取用户信息出错',
        type: 'error',
        duration: 3000
      })
      return Promise.reject(error)
    })
  },

  actionLogout: ({commit}) => {
    commit('setUserInfo', null)
    commit('setToken', null)
  }
}

const mutations = {
  setToken: (state, token) => {
    if (token) {
      cookie.setCookie(TOKEN_KEY, token)
    } else {
      cookie.removeCookie(TOKEN_KEY)
    }
    state.token = token
  },
  setUserInfo: (state, userInfo) => {
    state.userInfo = userInfo
  },
  setLoginRegisterModalVisible: (state, flag) => {
    state.loginRegisterModalVisible = flag
  },
  setActionIsLogin: (state, flag) => {
    state.actionIsLogin = flag || false
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}

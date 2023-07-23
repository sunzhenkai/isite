/* 用户相关API */
import request from '@/utils/request'

let API_URL = {
  obtainToken: 'auth-token/',
  users: 'users/',
  userInfo: 'user/info/'
}

export default {
  /**
   * 获取token及用户信息
   * @param data  ‘{username: '', password: ''}’
   */
  obtainToken: function (data) {
    return request({
      method: 'post',
      url: API_URL.obtainToken,
      data: data
    })
  },

  /**
   * 用户注册
   * @param data  ‘{username: username, password: password}’
   */
  register: function (data) {
    return request({
      method: 'post',
      url: API_URL.users,
      data: data
    })
  },

  obtainUserInfo: function () {
    return request ({
      method: 'get',
      url: API_URL.userInfo
    })
  }
}

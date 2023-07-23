import axios from 'axios'
import {Message} from 'element-ui'
import cookie, {TOKEN_KEY} from '@/utils/cookie'
import store from '@/store'

const service = axios.create({
  baseURL: process.env.BASE_URL,
  timeout: 15000
})

// request 拦截器
service.interceptors.request.use(config => {
  if (cookie.getCookie(TOKEN_KEY)) {
    config.headers = {
      'Authorization': 'Token ' + cookie.getCookie(TOKEN_KEY)
    }
  }
  return config
}, error => {
  console.log(error)
  Promise.reject(error)
})

// response 拦截器
service.interceptors.response.use(
  response => {
      return Promise.resolve(response.data)
  },
  error => {
    if (error && error.response.status === 401 && cookie.getCookie(TOKEN_KEY)) {
      cookie.removeCookie(TOKEN_KEY)
      store.dispatch('actionLogout')
      Message({
        message: '登录过期,请重新登录!',
        type: 'error',
        duration: 3000
      })
    } else {
      Message({
        message: error.response.data,
        type: 'error',
        duration: 3000
      })
    }
    return Promise.reject(error.response.data)
  }
)

export default service

import Cookies from 'js-cookie'

export const TOKEN_KEY= 'UserToken'
export const USER_INFO_KEY = 'UserInfo'

export default {
  getCookie: (key) => {
    return Cookies.get(key)
  },
  setCookie: (key, token) => {
    return Cookies.set(key, token)
  },
  removeCookie: (key) => {
    return Cookies.remove(key)
  }
}

/* store */

import Vue from 'vue'
import Vuex from 'vuex'
import UserStore from './modules/UserStore'
import ArticleInfoStore from './modules/ArticleInfoStore'
import CategoryStore from './modules/CategoryStore'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    UserStore,
    ArticleInfoStore,
    CategoryStore
  }
})

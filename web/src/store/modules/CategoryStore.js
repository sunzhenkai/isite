import ArticleApi from '@/api/ArticleApi'
import {Message} from 'element-ui'

const state = {
  categories: [],
}

const getters = {
  categories: (state) => {
    return state.categories
  }
}

const mutations = {
  setCategories: (state, {categories}) => {
    state.categories = categories
  }
}

const actions = {
  actionFetchCategories: ({commit, state}) => {
    if (state.categories.length === 0) {
      ArticleApi.obtainCategoryTree().then(res => {
        commit('setCategories', {categories: res})
      }).catch(error => {
        Message({
          message: error,
          type: 'error',
          duration: 3000
        })
      })
    }
  }
}


export default {
  state,
  getters,
  actions,
  mutations
}

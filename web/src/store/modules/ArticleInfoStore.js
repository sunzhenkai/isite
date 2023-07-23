import ArticleApi from '@/api/ArticleApi'
import {Message} from 'element-ui'

let defaultArticle = {
  title: '',
  summary: '',
  tags: [],
  category: [],
  content: '',
  content_type: 'MD',
  public: false
}

const state = {
  article: defaultArticle,
  isLoading: false
}

const getters = {
  article: (state) => {
    return state.article
  },
  isLoading: (state) => {
    return state.isLoading
  }
}

const mutations = {
  setArticle: (state, {article}) => {
    state.article = article
  },
  setLoading: (state, data) => {
    state.isLoading = data
  }
}

const actions = {
  actionSetArticle: ({commit, state}, {data}) => {
    commit('setArticle', data)
  },
  actionClearArticle: ({commit}) => {
    commit('setArticle', {article: defaultArticle})
  },
  actionFetchArticle: ({commit, state}, {id}) => {
    commit('setArticle', {article: defaultArticle})
    commit('setLoading', true)
    ArticleApi.obtainArticleDetail({id: id}).then(article => {
      commit('setArticle', {article: article})
      commit('setLoading', false)
    }).catch(error => {
      commit('setLoading', false)
      Message({
        message: error,
        type: 'error',
        duration: 3000
      })
    })
  }
}


export default {
  state,
  getters,
  actions,
  mutations
}

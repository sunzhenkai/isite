/* 文章相关 API */
import request from '@/utils/request'

let API_URL = {
  articles: 'articles/',
  categoryTree: 'article/category/tree/',
  summaryList: 'articles/',
  filterList: 'articles/filter/'
}

export default {
  submitArticle: function ({data}) {
    return request({
      method: data.id ? 'put' : 'post', // 新建或者更新
      url: API_URL.articles + (data.id ? data.id + '/' : ''),
      data: data
    })
  },
  obtainCategoryTree: function () {
    return request({
      method: 'get',
      url: API_URL.categoryTree
    })
  },
  obtainArticleSummaryList: function ({params, data}) {
    return request({
      method: 'get',
      url: API_URL.summaryList,
      data: data,
      params: params
    })
  },
  obtainArticleDetail: function ({id}) {
    return request({
      method: 'get',
      url: API_URL.articles + id + '/'
    })
  },
  filterArticle: function ({params, data}) {
    return request({
      method: 'get',
      url: API_URL.filterList,
      data: data,
      params: params
    })
  }
}

import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      redirect: 'article/list',
      name: 'index',
      component: () => import('@/views/layout/Layout'),
      children: [
        {
          path: 'article/write',
          name: 'writeArticle',
          component: () => import('@/views/article/WriteArticle')
        },
        {
          path: 'article/list',
          name: 'articleList',
          component: () => import('@/views/article/ArticleList')
        },
        {
          path: 'article/detail/:id',
          name: 'articleDetail',
          component: () => import('@/views/article/ArticleDetail')
        }
      ]
    }
  ]
})

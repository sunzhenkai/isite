<style lang="scss" scoped>

</style>

<template>
  <div>
    <el-row type="flex" justify="center" class="p-y-5">
      <el-col :lg="12" :md="16" :xs="20" :sm="20"
              class=" no-margin no-padding tags-container">
        <el-badge v-for="(count, tag) in statistics['tags']"
                  :key="Math.random()"
                  :tag="tag"
                  :value="count"
                  style="margin: .4rem .4rem;"
                  type="primary">
          <router-link :to="{path: '/article/list/?tag=' + encodeURIComponent(tag), params: {tag: tag}}">
            <el-button class="btn-tag" style="margin: -1px;" size="small">{{tag}}</el-button>
          </router-link>
        </el-badge>
      </el-col>
    </el-row>
    <el-row type="flex" justify="center">
      <el-col :lg="12" :md="16" :xs="20" :sm="20" class="border-default" style="background-color: white;">
        <div v-if="articles.length > 0">
          <article-list-item v-for="(item, index) in articles" :key="index" :articleInfo="item"></article-list-item>
          <el-pagination
            v-if="pageCount > 0"
            class="list-item-pagination"
            background
            layout="prev, pager, next"
            @current-change="onPageChange"
            :page-count="pageCount">
          </el-pagination>
        </div>
        <empty-tip v-else msg="没有获取到数据" style="margin-bottom: 2rem;"></empty-tip>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import ArticleApi from '@/api/ArticleApi'
  import ArticleListItem from './components/ArticleListItem'
  import EmptyTip from '../components/EmptyTip'

  export default {
    name: 'ArticleList',
    data: function () {
      return {
        page: 1,
        articles: [],
        pageCount: 0,
        statistics: {}
      }
    },
    methods: {
      getArticles: function () {
        let that = this
        ArticleApi.filterArticle({params: {page: that.page, tag: that.tag, cate: that.cate}}).then(res => {
          that.articles = res.results
          that.pageCount = res.pages
          that.statistics = res.statistics
        }).catch(error => {
          console.log(error)
        })
      },
      onPageChange: function (page) {
        this.page = page
        this.getArticles()
      }
    },
    created: function () {
      this.getArticles()
    },
    components: {EmptyTip, ArticleListItem},
    computed: {
      tag() {
        return this.$route.params.tag || this.$route.query.tag;
      },
      cate() {
        return this.$route.params.cate || this.$route.query.cate;
      }
    },
    watch: {
      tag() {
        this.page = 1
        this.getArticles()
      },
      cate() {
        this.page = 1
        this.getArticles()
      }
    }
  }
</script>

<template>
  <div>
    <el-row type="flex" justify="center">
      <el-col :lg="10" :md="12" :xs="20" :sm="20" class="border-default" style="background-color: white">
        <div class="content-top m-t-5">
          <h3 class="content-title">{{article.title}}</h3>
          <div class="content-tags">
            <router-link class="list-item-tag"
                         v-for="(tag, index) in article.tags"
                         :to="{path: '/article/list/?tag=' + encodeURIComponent(tag), params: {tag: tag}}"
                         :key="Math.random()">{{tag}}
            </router-link>
          </div>
          <div class="content-summary p-x-5">{{article.summary}}</div>
        </div>
        <div v-if="isArticleLoaded" class="p-x-5">
          <editor-md-show :article="article" :tocContainerId="tocElementId"></editor-md-show>
        </div>
        <div v-if="isLogin" class="content-bottom p-x-5 p-y-3" style="display: flex; justify-content: flex-end;">
          <a @click="onEditor" href="javascript: void(0)"><img class="bottom-img p-x-4"
                                                               src="/static/img/editor.png"></a>
          <!--          <a @click="onDelete" href="javascript: void(0)"><img class="bottom-img" src="/static/img/delete.png"></a>-->
        </div>
      </el-col>
      <el-col :lg="5" :md="5" class="m-l-10">
        <div class="border-default p-x-5" style="background-color: white;" id="tocContainerWrp">
          <p>目录</p>
          <div :id="tocElementId"></div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import ArticleApi from '@/api/ArticleApi'
  import EditorMdShow from './components/EditorMdShow'

  export default {
    name: 'ArticleDetail',
    data: function () {
      return {
        tocElementId: 'toc-container',
        article: {},
        isArticleLoaded: false
      }
    },
    methods: {
      setToCPosition: function () { // 设置目录位置
        let tocElement = document.getElementById('tocContainerWrp')
        tocElement && (tocElement.style.top = '' + (-document.body.getBoundingClientRect().y) + 'px')
      },
      onEditor: function () {
        this.$router.push({
          name: 'writeArticle',
          params: {
            'id': this.article.id,
            'article': this.article
          }
        })
      },
      onDelete: function () {
      },
      fetchArticleDetail: function () {
        let that = this
        return ArticleApi.obtainArticleDetail({id: this.id}).then(res => {
          that.article = res
          that.isArticleLoaded = true
        })
      }
    },
    components: {
      EditorMdShow
    },
    created: function () {
      let that = this
      window.addEventListener('scroll', () => { // 屏幕滚动
        that.setToCPosition()
      })
    },
    mounted: function () {
      this.fetchArticleDetail()
    },
    computed: {
      isLogin () {
        return this.$store.getters.isLogin
      },
      id () {
        return this.$route.params.id || this.$route.query.id
      }
    },
  }
</script>

<style lang="scss" scoped>
  #tocContainerWrp {
    position: relative;
    min-width: 25rem;
  }

  .bottom-img {
    width: 1.2rem;
  }
</style>

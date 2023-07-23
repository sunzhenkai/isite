<template>
  <div>
    <el-row v-if="article && categoryOptions">
      <article-write-header :article="article" :categoryOptions="categoryOptions"></article-write-header>
      <editor-md :article="article" :submitArticle="submitArticle" />
    </el-row>
  </div>
</template>

<script>
  import EditorMd from './components/EditorMd'
  import ArticleWriteHeader from './components/ArticleWriteHeader'
  import ArticleApi from '@/api/ArticleApi'
  import { Message } from 'element-ui'

  export default {
    name: "writeArticle",
    data: function () {
      return {
        article: this.$route.params.article || this.$route.query.article || {
          tags: []
        }
      }
    },
    components: {ArticleWriteHeader, EditorMd},
    methods: {
      submitArticle (isSubmit) {
        let that = this;
        ArticleApi.submitArticle({data: that.article}).then(res => {
          that.article.id = res.id;
          Message({
            message: '保存成功',
            type: 'success',
            duration: 1000
          });
          if (isSubmit) {
            that.$router.push({name: 'articleDetail', params: {id: that.article.id}})
          }
        }).catch(error => {
          console.log(error)
        })
      },
    },
    computed: {
      categoryOptions() {
        return this.$store.getters.categories;
      }
    }
  }


</script>

<style scoped>

</style>

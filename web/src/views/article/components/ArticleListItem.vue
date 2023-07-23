<!-- Article List Item -->
<style lang="scss" scoped>

</style>

<template>
  <div class="list-item-wrp">
    <router-link :to="{name: 'articleDetail', params: {id: articleInfo.id}}" class="list-item-title">{{articleInfo.title}}</router-link>
    <div class="list-item-summary">{{articleInfo.summary}}</div>
    <div class="list-item-tag-wrp">
      <router-link class="list-item-tag"
                   v-for="(tag, index) in articleInfo.tags"
                   :to="{path: '/article/list/?tag=' + encodeURIComponent(tag), params: {tag: tag}}"
                   :key="Math.random()">{{tag}}</router-link>
    </div>
    <div class="list-item-suffix">
      <span>{{formatDateString(articleInfo.update_datetime)}}</span>
      <span>{{articleInfo.author ? articleInfo.author.username : ''}}</span>
    </div>
  </div>
</template>

<script>
  import {formatDate} from '@/utils/tools'

  export default {
    name: 'ArticleListItem',
    props: {
      articleInfo: {
        type: Object
      }
    },
    methods: {
      formatDateString: function (dt) {
        return formatDate(new Date(dt))
      }
    }
  }
</script>

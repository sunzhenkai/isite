<template>
  <div>
    <el-input v-model="article.title" placeholder="请输入标题">
      <template slot="prepend">标题</template>
    </el-input>
    <el-input class="m-y-4" v-model="article.summary" placeholder="请输入概述">
      <template slot="prepend">概述</template>
    </el-input>
    <div class="m-y-4" style="width: 100%; display: flex;">
      <div class="flex-align-center">
        <div class="row-info-prepend" style="border-right: none;">分类</div>
        <el-cascader class="category-selector-wrp"
                     placeholder="请选择"
                     :options="categoryOptions"
                     :props="{value: 'id', label: 'name'}"
                     v-model="articleCategory"
        ></el-cascader>
      </div>
      <div class="flex-align-center p-l-5">
        <!--<div class="row-info-prepend" style="border-right: none;">公开</div>-->
        <el-switch
          class="category-selector-wrp"
          v-model="article.public"
          inactive-text="私密"
          active-text="公开">
        </el-switch>
      </div>
      <div style="flex: 1;" class="p-l-5 no-padding no-margin">
        <div class="row-info">
          <div class="row-info-prepend">标签</div>
          <!-- 标签展示 -->
          <div class="row-info-suffix">
            <!-- 已输入标签 -->
            <el-tag
              :key="index"
              v-for="(tag, index) in article.tags"
              closable
              :disable-transitions="false"
              @close="handleTagInputClose(tag)">
              {{tag}}
            </el-tag><!-- /已输入标签 -->

            <input
              class="input-new-tag border-default"
              v-if="tagInputVisible"
              v-model="tagInputValue"
              ref="saveTagInput"
              @keyup.enter="handleTagInputConfirm"
              @blur="handleTagInputConfirm"
              title="tag-name-input"/>
            <el-button v-else class="button-new-tag" size="small" @click="showTagInput">+标签</el-button>
          </div><!-- /标签展示 -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'ArticleWriteHeader',
    data () {
      return {
        tagInputVisible: false,
        tagInputValue: ''
      }
    },
    props: {
      categoryOptions: {
        type: Array,
        default: []
      },
      article: {
        type: Object,
        default: {}
      }
    },
    methods: {
      handleTagInputClose (tag) {
        this.article.tags.splice(this.article.tags.indexOf(tag), 1)
      },

      showTagInput () {
        this.tagInputVisible = true
        this.$nextTick(_ => {
          this.$refs.saveTagInput.focus()
        })
      },

      handleTagInputConfirm () {
        let inputValue = this.tagInputValue.trim()
        if (inputValue) {
          this.article.tags.push(inputValue)
        }
        this.tagInputVisible = false
        this.tagInputValue = ''
      },
      getCatePath (nodes, id) {   // 递归获取嵌套 category path
        for (let i = 0; i < nodes.length; ++i) {
          let node = nodes[i]
          if (node.id === id) {
            return [node.id]
          } else if (node.children && node.children.length > 0) {
            let recursion = this.getCatePath(node.children, id)
            if (recursion && recursion.length > 0) {
              recursion.push(node.id)
              return recursion
            }
          }
        }
        return null
      }
    },
    computed: {
      articleCategory: {
        get () {
          return this.article.category
        },
        set (data) {
          if (data && data.length > 0) {
            this.article.category = data[data.length-1]
          }
        }
      }
    }
  }
</script>


<style lang="scss" scoped>
  .el-tag {
    margin-left: 10px;
  }

  .button-new-tag {
    margin-left: 10px;
    height: 28px;
    line-height: 28px;
    padding-top: 0;
    padding-bottom: 0;
  }

  .input-new-tag {
    width: 65px;
    margin-left: 10px;
    line-height: 24px;
    padding: 0 8px;
    font-size: 12px;
    color: #909399;

    &:focus {
      border-color: #409eff;
      outline: none;
    }
  }
</style>

<style lang="scss">
  .category-selector-wrp {
    input {
      border-bottom-left-radius: 0;
      border-top-left-radius: 0;
    }
  }
</style>

<template>
  <div id="editor-md">
    <link href="/static/editormd/css/editormd.min.css" rel="stylesheet">
    <textarea style="display:none" title="content-text"></textarea>
  </div>
</template>

<script>
  import {fetchScript} from '../../../utils/tools'
  import {Loading} from 'element-ui'
  import {defaultEditorConfig} from '../../../config/tool/EditorMdConfig'
  import {mapState} from 'vuex'

  export default {
    name: 'EditorMd',
    data () {
      let that = this
      return {
        loadingInstance: Loading.service({
          target: '#appMain'
        }),
        editor: null,
        isEditorLoaded: false,
        editorConfig: {
          ...defaultEditorConfig,   // 引入默认配置
          onchange: function () {
            that.$nextTick(() => {  // 异步绑定
              that.article.content = this.getValue()
            })
          },
          toolbarHandlers: {
            save: function () {
              that.submitArticle()
            },
            submit: function () {
              that.article.public = true
              that.submitArticle(true)
            }
          }
        }
      }
    },
    props: {
      submitArticle: {
        type: Function
      },
      article: {
        type: Object,
        default: {
          title: '',
          tags: [],
          category: []
        }
      }
    },
    mounted () {
      this.initEditor()
      this.$nextTick(() => { // 以服务的方式调用的 Loading 需要异步关闭
        this.loadingInstance.close()
      })
    },
    methods: {
      initEditor () {   // 初始化编辑器
        let that = this;
        (async () => {
          await fetchScript('/static/editormd/js/jquery.min.js')
          await fetchScript('/static/editormd/js/zepto.min.js')
          await fetchScript('/static/editormd/js/editormd.min.js')

          that.$nextTick((editorMD = window.editormd) => {
            that.editor = editorMD('editor-md', {
              ...that.editorConfig,
              // autoHeight: true,
              onload: function () {
                let content = that.article.content
                that.isEditorLoaded = true
                that.editor.setMarkdown(content)
              }
            })
          })
        })()
      }
    },
    // computed: {
    //   article () {
    //     return this.$store.getters.article
    //   }
    // },
    // watch: {
    //   article () {
    //     let content = this.$store.getters.article.content
    //     let that = this
    //     if (that.isEditorLoaded) {
    //       that.editor.setCursor({line:1, ch:1})
    //       that.editor.insertValue(content)
    //       that.editor.setMarkdown(content)
    //     }
    //   }
    // }
  }
</script>

<style scoped>

</style>

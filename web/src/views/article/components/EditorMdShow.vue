<style lang="scss" scoped>
  #editormd-view {
    padding: 15px 0 !important;
  }
</style>

<template>
  <div id="editormd-view">
    <link href="/static/editormd/css/editormd.min.css" rel="stylesheet">
    <textarea style="display:none;" name="editormd-markdown-doc"></textarea>
  </div>
</template>

<script>
  import { fetchScript } from '../../../utils/tools'
  import {mdViewerConfig} from '../../../config/tool/EditorMdConfig'

  export default {
    name: 'EditorMdShow',
    data() {
      return {
        editor: null,
        isEditorLoaded: false
      }
    },
    props: {
      editorPath: {
        type: String,
        default: '/static/editormd'
      },
      tocContainerId: {
        type: String
      },
      article: {
        type: Object,
        default: {}
      }
    },
    mounted () {
      (async () => {
        await fetchScript('/static/editormd/js/jquery.min.js');
        await fetchScript('/static/editormd/js/zepto.min.js');
        await fetchScript('/static/editormd/lib/marked.min.js');
        await fetchScript('/static/editormd/lib/prettify.min.js');
        await fetchScript('/static/editormd/lib/raphael.min.js');
        await fetchScript('/static/editormd/lib/underscore.min.js');
        await fetchScript('/static/editormd/lib/sequence-diagram.min.js');
        await fetchScript('/static/editormd/lib/flowchart.min.js');
        await fetchScript('/static/editormd/lib/jquery.flowchart.min.js');
        await fetchScript('/static/editormd/js/editormd.min.js');

        this.initEditor();
      })();
    },
    methods: {
      initEditor () {
        let that = this;
        this.$nextTick((editorMD = window.editormd) => {
          if (editorMD) {
            setTimeout(function () {
              that.editor = editorMD.markdownToHTML('editormd-view',
                {...mdViewerConfig,
                  markdown: that.article.content,
                  tocContainer: '#' + that.tocContainerId,
                  onload: function () {
                    let content = that.article
                    that.isEditorLoaded = true
                    that.editor.setMarkdown(content)
                  }
                }, 500);
            });
          }
        });
      }
    }
  }
</script>

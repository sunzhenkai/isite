export const defaultEditorConfig = {  // 编辑器配置
  height: 600,
  path: '/static/editormd/lib/', // Autoload modules mode, codemirror, marked... dependents libs path
  codeFold: true,
  saveHTMLToTextarea: true,
  placeholder: '',
  searchReplace: true,
  htmlDecode: 'style,script,iframe|on*',
  taskList: true,
  tocm: true,                  // Using [TOCM]
  tex: true,                   // 开启科学公式TeX语言支持，默认关闭
  flowChart: true,             // 开启流程图支持，默认关闭
  sequenceDiagram: true,       // 开启时序/序列图支持，默认关闭,
  imageUpload: true,
  imageFormats: ['jpg', 'jpeg', 'gif', 'png', 'bmp', 'webp'],
  imageUploadURL: '/api/upload/image/',

  toolbarIcons: function () {
    return ['save', 'submit', '|',
      'undo', 'redo', '|', 'bold', 'del', 'italic', 'quote', 'uppercase', 'lowercase', '|',
      'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'list-ul', 'list-ol', 'hr', '|',
      'link', 'reference-link',
      'image', 'code', 'preformatted-text', 'code-block',
      'table', 'datetime', 'html-entities', 'pagebreak', '|',
      'goto-line', 'watch', 'preview', 'search', 'fullscreen', 'clear', 'help'
    ]
  },
  toolbarIconsClass: {
    save: 'fa-save',
    submit: 'fa-upload'
  },
  lang: {
    toolbar: {
      save: '保存',
      submit: '提交'
    }
  }
};

export const mdViewerConfig = {
  // markdown        : that.articleInfo.content ,//+ "\r\n" + $("#append-test").text(),
  htmlDecode      : "style,script,iframe",  // you can filter tags decode
  tocm            : true,    // Using [TOCM]
  taskList        : true,
  tex             : true,  // 默认不解析
  flowChart       : true,  // 默认不解析
  sequenceDiagram : true,  // 默认不解析
};

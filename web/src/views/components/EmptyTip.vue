<style lang="scss" scoped>
.empty-tip {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 30px;

  img {
    width: 60px;
    height: 60px;
  }

  p {
    font-size: .8rem;
    color: gray;
    margin: 0;
  }
}
</style>

<template>
  <div class="empty-tip" v-if="show">
    <img :src="EmptyIcon" v-if="showImg"/>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import SadIcon from '@/assets/icon/sad.png'

export default {
  name: 'EmptyTip',
  data: function () {
    return {
      EmptyIcon: SadIcon
    }
  },
  props: {
    show: {
      type: Boolean,
      default: true
    },
    showImg: {
      type: Boolean,
      default: true
    },
    msg: {
      type: String,
      default: '没有获取到更多数据'
    }
  }
}
</script>

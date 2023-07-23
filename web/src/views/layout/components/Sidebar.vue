<style lang="scss" scoped>
</style>

<template>
    <el-menu :collapse="isCollapse" style="height: 100%;">
        <el-menu-item style="text-align: center;">
            <icon name="bars"></icon>
        </el-menu-item>
        <el-menu-item index="2">
            <i class="el-icon-menu"></i>
            <span slot="title">导航二</span>
        </el-menu-item>
        <el-menu-item index="3" disabled>
            <i class="el-icon-document"></i>
            <span slot="title">导航三</span>
        </el-menu-item>
        <el-menu-item index="4">
            <i class="el-icon-setting"></i>
            <span slot="title">导航四</span>
        </el-menu-item>
    </el-menu>
</template>

<script>
export default {
    name: 'SidebarComponent',
    data: function () {
        return {
            isCollapse: true
        }
    }
}
</script>


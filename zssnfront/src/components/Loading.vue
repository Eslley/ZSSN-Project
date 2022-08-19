<template>
    <div class="loading">
        <div v-if="isLoading" class="preloader-wrapper big active">
            <div class="spinner-layer spinner-blue-only">
                <div class="circle-clipper left">
                    <div class="circle"></div>
                </div><div class="gap-patch">
                    <div class="circle"></div>
                </div><div class="circle-clipper right">
                    <div class="circle"></div>
                </div>
            </div>
            
        </div>
    </div>
</template>

<script>

    export default {
        name: "Loading",
        props: {
            isLoading: false
        }
    }

</script>

<style>

    .loading {
        position: fixed;
        top: 50%;
        left: 50%;
        margin: -25px 0 0 -25px;left: 50%;
        top: 50%;
        background-color: rgba(0, 0reen, 0lue, 0.5);
    } 

</style>

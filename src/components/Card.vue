<template>
  <div class="main">
    <Unit v-for="photo in state.APIData" :key="photo.id" :photo="photo"></Unit>
  </div>
</template>

<script>
import { onMounted, reactive, defineAsyncComponent } from "vue";
import { getAPI } from "@/axios_api";

const Loading = () => import("@/components/Loading");

const Unit = defineAsyncComponent({
  loader: () => import("@/components/Unit" /* webpackChunkName: "Unit" */),
  loadingComponent: Loading,
  delay: 500,
});

export default {
  name: "Card",
  setup() {
    const state = reactive({
      APIData: {},
    });

    const setAll = async () => {
      try {
        const getPost = await getAPI.get("/api/images/");
        state.APIData = getPost.data;
      } catch (err) {
        console.log(err);
      }
    };

    onMounted(() => {
      setAll();
    });
    return {
      state,
    };
  },
  components: {
    Unit,
  },
};
</script>

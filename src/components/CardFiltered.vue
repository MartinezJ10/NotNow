<template>
  <div class="main">
    <Unit v-for="photo in state.APIData" :key="photo.id" :photo="photo"></Unit>
  </div>
</template>

<script>
import { reactive, computed, onMounted, defineAsyncComponent } from "vue";
import { useRoute } from "vue-router";
import { getAPI } from "@/axios_api";

import Loading from "@/components/Loading";

const Unit = defineAsyncComponent({
  loader: () =>
    import("@/components/Unit" /* webpackChunkName: "UnitFilter" */),
  loadingComponent: Loading,
  delay: 500,
});

export default {
  name: "CardFiltered",
  components: {
    Unit,
  },
  setup() {
    const state = reactive({
      APIData: [],
    });
    const route = useRoute();

    const id = computed(() => route.params.id);

    const CardsFiltered = async () => {
      try {
        const resp = await getAPI.get(`/api/categoryFilter/${id.value}/`);
        state.APIData = resp.data;
      } catch (err) {
        console.log(err);
      }
    };
    onMounted(() => {
      CardsFiltered();
    });

    return {
      state,
    };
  },
};
</script>

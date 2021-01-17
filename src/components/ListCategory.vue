<template>
  <div class="categoryBlock">
    <Category
      v-for="category in state.category"
      :key="category.id"
      :category="category"
    />
  </div>
</template>

<script>
import { defineAsyncComponent, onMounted, reactive } from "vue";
import { getAPI } from "@/axios_api";

const Category = defineAsyncComponent(() =>
  import("@/components/Category" /* webpackChunkName: "Category" */)
);

export default {
  name: "ListCategory",
  components: {
    Category,
  },
  setup() {
    const state = reactive({
      category: {},
    });

    const showCategories = async () => {
      const resp = await getAPI.get("/api/category/");
      state.category = resp.data;
    };

    onMounted(() => {
      showCategories();
    });
    return {
      state,
    };
  },
};
</script>

<template>
  <Detailed />
</template>

<script>
import { defineAsyncComponent } from "vue";

const Detailed = defineAsyncComponent(() =>
  import("@/components/Detailed" /* webpackChunkName: "Detailed" */)
);

export default {
  name: "Detail",
  components: {
    Detailed,
  },
};
</script>

<style></style>

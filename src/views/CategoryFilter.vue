<template>
  <Nav />
  <CardFiltered />
</template>

<script>
import { defineAsyncComponent } from "vue";

const CardFiltered = defineAsyncComponent(() =>
  import("@/components/CardFiltered" /* webpackChunkName: "CardFiltered" */)
);
const Nav = defineAsyncComponent(() =>
  import("@/components/Nav" /* webpackChunkName: "Nav" */)
);
export default {
  components: {
    CardFiltered,
    Nav,
  },
};
</script>

<style></style>

<template>
  <Nav />
  <Card />
</template>

<script>
import { defineAsyncComponent } from "vue";

const Card = defineAsyncComponent(() =>
  import("@/components/Card" /* webpackChunkName: "Card" */)
);
const Nav = defineAsyncComponent(() =>
  import("@/components/Nav" /* webpackChunkName: "Nav" */)
);

export default {
  name: "Gallery",
  components: {
    Nav,
    Card,
  },
};
</script>

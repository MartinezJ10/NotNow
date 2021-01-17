<template>
  <router-link :to="{ name: 'CategoyFilter', params: { id: category.id } }">
    <div class="category">
      <h5>{{ category.name }}</h5>
    </div>
  </router-link>
</template>

<script>
export default {
  name: "Category",
  props: {
    category: Object,
  },
};
</script>

<style></style>

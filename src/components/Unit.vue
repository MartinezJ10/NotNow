<template>
  <router-link :to="{ name: 'Detail', params: { id: photo.id } }">
    <div class="block">
      <div class="textBlock">
        <h3>{{ photo.title }}</h3>
      </div>
      <div class="imgBlock">
        <img v-lazy="photo.image" :alt="photo.alt" />
      </div>
    </div>
  </router-link>
</template>

<script>
export default {
  name: "Unit",
  props: {
    photo: Object,
  },
};
</script>

<style></style>

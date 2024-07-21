<script setup lang="ts">
import McuConfigList from "@/components/McuConfigList.vue";
</script>

<template>
  <header>
    <div class="wrapper">
    </div>
  </header>
  <Suspense>
    <McuConfigList source_filename="kconfigs.json"></McuConfigList>
    <template #fallback>
      Loading... Please Wait
    </template>
  </suspense>
  <main>
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>

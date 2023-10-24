





<!DOCTYPE html>
<html lang="en" data-color-mode="auto" data-light-theme="dark_dimmed" data-dark-theme="dark_dimmed"  data-a11y-animated-images="system" data-a11y-link-underlines="true">

    <style>
  /* for each iteration, uncomment the CSS variable */

  /* light themes */
  [data-color-mode="light"][data-light-theme*="light"],
  [data-color-mode="auto"][data-light-theme*="light"] {
    /* iteration 1 */
    --border-color-iteration-1: #C8CCD0;
    /* iteration 2 */
    --border-color-iteration-2: #BABFC5;
    /* iteration 3 */
    --border-color-iteration-3: #A6ADB4;
    /* iteration final */
    --border-color-iteration-4: #8D969F;

    /* the first value is the final step, which falls back to previous iterations */
    --control-borderColor-rest: var(--border-color-iteration-4, var(--border-color-iteration-3, var(--border-color-iteration-2, var(--border-color-iteration-1)))) !important;
  }

  /* dark themes */
  [data-color-mode="dark"][data-dark-theme*="dark"],
  [data-color-mode="auto"][data-light-theme*="dark"] {
    /* iteration 1 */
    --border-color-iteration-1: #363940;
    /* iteration 2 */
    --border-color-iteration-2: #3F434B;
    /* iteration 3 */
    --border-color-iteration-3: #4B5159;
    /* iteration final */
    --border-color-iteration-4: #5b626c;

    /* the first value is the final step, which falls back to previous iterations */
    --control-borderColor-rest: var(--border-color-iteration-4, var(--border-color-iteration-3, var(--border-color-iteration-2, var(--border-color-iteration-1)))) !important;
  }

  [data-color-mode="dark"][data-dark-theme="dark_dimmed"],
  [data-color-mode="dark"][data-dark-theme="light_high_contrast"],
  [data-color-mode="dark"][data-dark-theme="dark_high_contrast"],
  [data-color-mode="light"][data-light-theme="dark_dimmed"],
  [data-color-mode="light"][data-light-theme="light_high_contrast"],
  [data-color-mode="light"][data-light-theme="dark_high_contrast"] {
    /* skip these themes, use the fallback */
    --control-borderColor-rest: initial !important;
  }

  @media (prefers-color-scheme: dark) {
    /* dark colors in dark mode */
    [data-color-mode="auto"][data-dark-theme*="dark"] {
      /* iteration 1 */
      --border-color-iteration-1: #363940;
      /* iteration 2 */
      --border-color-iteration-2: #3F434B;
      /* iteration 3 */
      --border-color-iteration-3: #4B5159;
      /* iteration final */
      --border-color-iteration-4: #5b626c;

      /* the first value is the final step, which falls back to previous iterations */
      --control-borderColor-rest: var(--border-color-iteration-4, var(--border-color-iteration-3, var(--border-color-iteration-2, var(--border-color-iteration-1)))) !important;
    }

    /* light colors in dark mode */
    [data-color-mode="auto"][data-dark-theme*="light"] {
      /* iteration 1 */
      --border-color-iteration-1: #C8CCD0;
      /* iteration 2 */
      --border-color-iteration-2: #BABFC5;
      /* iteration 3 */
      --border-color-iteration-3: #A6ADB4;
      /* iteration final */
      --border-color-iteration-4: #8D969F;

      /* the first value is the final step, which falls back to previous iterations */
      --control-borderColor-rest: var(--border-color-iteration-4, var(--border-color-iteration-3, var(--border-color-iteration-2, var(--border-color-iteration-1)))) !important;
      }

    [data-color-mode="auto"][data-dark-theme="dark_dimmed"],
    [data-color-mode="auto"][data-dark-theme="light_high_contrast"],
    [data-color-mode="auto"][data-dark-theme="dark_high_contrast"] {
      /* skip these themes, use the fallback */
      --control-borderColor-rest: initial !important;
    }
  }

  @media (prefers-color-scheme: light) {
    /* dark colors in light mode */
    [data-color-mode="auto"][data-light-theme*="dark"] {
      /* iteration 1 */
      --border-color-iteration-1: #363940;
      /* iteration 2 */
      --border-color-iteration-2: #3F434B;
      /* iteration 3 */
      --border-color-iteration-3: #4B5159;
      /* iteration final */
      --border-color-iteration-4: #5b626c;

      /* the first value is the final step, which falls back to previous iterations */
      --control-borderColor-rest: var(--border-color-iteration-4, var(--border-color-iteration-3, var(--border-color-iteration-2, var(--border-color-iteration-1)))) !important;
    }

    /* light colors in light mode */
    [data-color-mode="auto"][data-light-theme*="light"] {
      /* iteration 1 */
      --border-color-iteration-1: #C8CCD0;
      /* iteration 2 */
      --border-color-iteration-2: #BABFC5;
      /* iteration 3 */
      --border-color-iteration-3: #A6ADB4;
      /* iteration final */
      --border-color-iteration-4: #8D969F;

      /* the first value is the final step, which falls back to previous iterations */
      --control-borderColor-rest: var(--border-color-iteration-4, var(--border-color-iteration-3, var(--border-color-iteration-2, var(--border-color-iteration-1)))) !important;
    }

    [data-color-mode="auto"][data-light-theme="dark_dimmed"],
    [data-color-mode="auto"][data-light-theme="light_high_contrast"],
    [data-color-mode="auto"][data-light-theme="dark_high_contrast"] {
      /* skip these themes, use the fallback */
      --control-borderColor-rest: initial !important;
    }
  }
</style>


  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">
  <link rel="preconnect" href="https://github.githubassets.com" crossorigin>
  <link rel="preconnect" href="https://avatars.githubusercontent.com">

  


  <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/dark_dimmed-27c8d635e4e5.css" /><link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/dark_dimmed-27c8d635e4e5.css" /><link data-color-theme="light" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light-b92e9647318f.css" /><link data-color-theme="dark" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark-5d486a4ede8e.css" /><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-8438e75afd36.css" /><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-bf5665b96628.css" /><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-c414b5ba1dce.css" /><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-e5868b7374db.css" /><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-299ac9c64ec0.css" /><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-3a26e78ad0ff.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-primitives-363ec1831c26.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-ba77178b8574.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/global-88a58e1d2695.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/github-998500536919.css" />
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/code-71ecd5638fbf.css" />

  

  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["copilot_conversational_ux_streaming","failbot_handle_non_errors","geojson_azure_maps","hovercard_show_on_focus","image_metric_tracking","repository_suggester_elastic_search","turbo_experiment_risky","sample_network_conn_type","star_button_focus"]}</script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/wp-runtime-67360fd65b00.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_dompurify_dist_purify_js-64d590970fa6.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_stacktrace-parser_dist_stack-trace-parser_esm_js-node_modules_github_bro-a4c183-18bf85b8e9f4.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/ui_packages_soft-nav_soft-nav_ts-bbaed7e6fb42.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/environment-fc6543d75794.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_selector-observer_dist_index_esm_js-2646a2c533e3.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_focus-zone_js-d55308df5023.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_relative-time-element_dist_index_js-99e288659d4f.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_fzy_js_index_js-node_modules_github_combobox-nav_dist_index_js-node_modu-344bff-91b70bb50d68.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_details-dialog-elemen-29dc30-2a5b7c1aa525.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-59c459-4aa3ec97e0dc.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_primer_view-co-2c6968-46264b1e620c.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/github-elements-3485f2997bc6.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/element-registry-1105ae3b6f33.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_catalyst_lib_index_js-node_modules_github_hydro-analytics-client_-978abc0-d5b921292620.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_lit-html_lit-html_js-4ccebb6ebf7d.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_alive-client_dist-bf5aa2-504c8d53fb8e.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_morphdom_dist_morphdom-esm_js-b1fdd7158cf0.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_turbo_dist_turbo_es2017-esm_js-9a3541181451.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_color-convert_index_js-35b3ae68c408.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_dimensions_js-node_modules_github_hotkey_dist_-8755d2-f721427ba08d.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_session-resume_dist_index_js-node_modules_primer_behaviors_dist_e-ac74c6-4e7cf4e77afd.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_paste-markdown_dist_index_esm_js-node_modules_github_quote-select-854ff4-b4a2793be3fe.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_details-dialog_ts-app_assets_modules_github_fetch_ts-311ea0d6e989.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_updatable-content_ts-ui_packages_hydro-analytics_hydro-analytics_ts-a50bfd286a4c.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_behaviors_task-list_ts-app_assets_modules_github_onfocus_ts-app_ass-079b43-971d727bc4a9.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_sticky-scroll-into-view_ts-00ce2dd9370d.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_include-2e2258-c320637f605b.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-db335a626783.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/behaviors-fa049e3bdc0e.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-623425af41e1.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/notifications-global-6997e0de353e.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/code-menu-6bd50a0647d6.js"></script>
  
  <script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/react-lib-26cb888452e9.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_octicons-react_dist_index_esm_js-node_modules_primer_react_lib-es-2e8e7c-b8c027e1cfac.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Box_Box_js-96a44addc402.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Button_Button_js-node_modules_primer_react_lib-esm_-f6da63-8ede4ca7129a.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_node_modules_primer_octicons-react_dist_index_esm_js-03b6dd82d40a.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Button_index_js-node_modules_primer_react_lib-esm_O-701f13-047a44a18d3a.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Text_Text_js-node_modules_primer_react_lib-esm_Text-85a14b-0f28951279b7.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_ActionList_index_js-f25d88d57fbb.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_ActionMenu_ActionMenu_js-2f08ef908241.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_behaviors_dist_esm_scroll-into-view_js-node_modules_primer_react_-04bb1b-a6096689d2d5.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_FormControl_FormControl_js-6cc99a41ba59.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_react-router-dom_dist_index_js-4a785319b497.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_PageLayout_PageLayout_js-19e7585e47dd.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Dialog_js-node_modules_primer_react_lib-esm_Flash_F-ad64b6-f3217651e114.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_UnderlineNav2_index_js-b739f40cf454.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Avatar_Avatar_js-node_modules_primer_react_lib-esm_-9bd36c-ba57d123ed28.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_AvatarStack_AvatarStack_js-node_modules_primer_reac-6d3540-8d6aa4909850.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_primer_react_lib-esm_Breadcrumbs_Breadcrumbs_js-node_modules_primer_reac-a97071-8654e95e07c0.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/ui_packages_react-core_create-browser-history_ts-ui_packages_react-core_deferred-registry_ts--ebbb92-dd46f515ed6d.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/ui_packages_react-core_register-app_ts-c960459705f5.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/ui_packages_paths_index_ts-8dc346e26764.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/ui_packages_ref-selector_RefSelector_tsx-43e70e7c0d33.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_blob-anchor_ts-app_assets_modules_github_filter-sort_ts-app_assets_-681869-26ce2427d133.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/ui_packages_commit-attribution_index_ts-ui_packages_commit-checks-status_index_ts-ui_packages-cc11d2-c825eaeae7ef.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_react-code-view_pages_CodeView_tsx-1b0411d02a7f.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/react-code-view-e6098665e216.js"></script>


  <title>twisted/README.rst at trunk · twisted/twisted</title>



  <meta name="route-pattern" content="/:user_id/:repository/blob/*name(/*path)">

    
  <meta name="current-catalog-service-hash" content="82c569b93da5c18ed649ebd4c2c79437db4611a6a1373e805a3cb001c64130b7">


  <meta name="request-id" content="88DC:053D:09A3:0B01:6537BE98" data-turbo-transient="true" /><meta name="html-safe-nonce" content="8c2051005ffd010f46b22c70f7648a6aedd3acd428da6bddf6817725dcdee97a" data-turbo-transient="true" /><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS90d2lzdGVkL3R3aXN0ZWQiLCJyZXF1ZXN0X2lkIjoiODhEQzowNTNEOjA5QTM6MEIwMTo2NTM3QkU5OCIsInZpc2l0b3JfaWQiOiI0NTk3MDg0NjczMjA2NTEzMDU5IiwicmVnaW9uX2VkZ2UiOiJmcmEiLCJyZWdpb25fcmVuZGVyIjoiaWFkIn0=" data-turbo-transient="true" /><meta name="visitor-hmac" content="dde4588feb90b9d47060975af1564d6dc001277adddf5eb7c38c0a5f5c61c3c4" data-turbo-transient="true" />


    <meta name="hovercard-subject-tag" content="repository:1985358" data-turbo-transient>


  <meta name="github-keyboard-shortcuts" content="repository,source-code,file-tree" data-turbo-transient="true" />
  

  <meta name="selected-link" value="repo_source" data-turbo-transient>
  <link rel="assets" href="https://github.githubassets.com/">

    <meta name="google-site-verification" content="c1kuD-K2HIVF635lypcsWPoD4kilo5-jA_wBFyT4uMY">
  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
  <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
  <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">
  <meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I">

<meta name="octolytics-url" content="https://collector.github.com/github/collect" /><meta name="octolytics-actor-id" content="16610768" /><meta name="octolytics-actor-login" content="AleksNeStu" /><meta name="octolytics-actor-hash" content="621feba9dd7feb5723472e8a11dd05134c8df9d0b3eb2840667dcfa93f8c88ed" />

  <meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-turbo-transient="true" />

  




  

    <meta name="user-login" content="AleksNeStu">

  <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="viewport" content="width=device-width">
    
      <meta name="description" content="Event-driven networking engine written in Python. Contribute to twisted/twisted development by creating an account on GitHub.">
      <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <meta property="fb:app_id" content="1401488693436528">
    <meta name="apple-itunes-app" content="app-id=1477376905, app-argument=https://github.com/twisted/twisted/blob/trunk/README.rst" />
      <meta name="twitter:image:src" content="https://opengraph.githubassets.com/46e90a02cace02402fa82056cb911182cb882f468cd5b8bd9b49288842611d06/twisted/twisted" /><meta name="twitter:site" content="@github" /><meta name="twitter:card" content="summary_large_image" /><meta name="twitter:title" content="twisted/README.rst at trunk · twisted/twisted" /><meta name="twitter:description" content="Event-driven networking engine written in Python. Contribute to twisted/twisted development by creating an account on GitHub." />
      <meta property="og:image" content="https://opengraph.githubassets.com/46e90a02cace02402fa82056cb911182cb882f468cd5b8bd9b49288842611d06/twisted/twisted" /><meta property="og:image:alt" content="Event-driven networking engine written in Python. Contribute to twisted/twisted development by creating an account on GitHub." /><meta property="og:image:width" content="1200" /><meta property="og:image:height" content="600" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="twisted/README.rst at trunk · twisted/twisted" /><meta property="og:url" content="https://github.com/twisted/twisted/blob/trunk/README.rst" /><meta property="og:description" content="Event-driven networking engine written in Python. Contribute to twisted/twisted development by creating an account on GitHub." />
      

      <link rel="shared-web-socket" href="wss://alive.github.com/_sockets/u/16610768/ws?session=eyJ2IjoiVjMiLCJ1IjoxNjYxMDc2OCwicyI6MTIxNzY0MzY2MSwiYyI6MzU2OTQ1OTM1NiwidCI6MTY5ODE1MjA4OH0=--1907b4650da2939553a6a617df1dd31293ba04db63dd8c51c5e2186234c5db17" data-refresh-url="/_alive" data-session-id="6a238eb2ef98c3d1a382ea0e63c029bb6e29cc3aee81f6e3395d7eb761907a2e">
      <link rel="shared-web-socket-src" href="/assets-cdn/worker/socket-worker-cee473359cfe.js">


        <meta name="hostname" content="github.com">


      <meta name="keyboard-shortcuts-preference" content="all">

        <meta name="expected-hostname" content="github.com">


  <meta http-equiv="x-pjax-version" content="616aa1074bc2a18becb89cc483ffa68a7b68c083933d16e6bb2c772c60db0e38" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="ee14a7165914197d62e19f664bfb961fcfdfc1ec31939a5c7b137fbab1751c87" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="ad14cf200d2f78210fb816034f5ae43a1a3744f760940dc4dc9062516d20e0d2" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="3b6ad0ae3d5d92cd345c7bd69b2973b27e5bc8049aa3507f11905509dceb9eaa" data-turbo-track="reload">

  <meta name="turbo-cache-control" content="no-preview" data-turbo-transient="">

      <meta name="turbo-cache-control" content="no-cache" data-turbo-transient>
    <meta data-hydrostats="publish">

  <meta name="go-import" content="github.com/twisted/twisted git https://github.com/twisted/twisted.git">

  <meta name="octolytics-dimension-user_id" content="716546" /><meta name="octolytics-dimension-user_login" content="twisted" /><meta name="octolytics-dimension-repository_id" content="1985358" /><meta name="octolytics-dimension-repository_nwo" content="twisted/twisted" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="1985358" /><meta name="octolytics-dimension-repository_network_root_nwo" content="twisted/twisted" />



  <meta name="turbo-body-classes" content="logged-in env-production page-responsive">


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <meta name="browser-optimizely-client-errors-url" content="https://api.github.com/_private/browser/optimizely_client/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/assets/pinned-octocat-093da3e6fa40.svg" color="#000000">
  <link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png">
  <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg">

<meta name="theme-color" content="#1e2327">
<meta name="color-scheme" content="light dark" />


  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-in env-production page-responsive" style="word-wrap: break-word;">
    <div data-turbo-body class="logged-in env-production page-responsive" style="word-wrap: break-word;">
      


    <div class="position-relative js-header-wrapper ">
      <a href="#start-of-content" class="p-3 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>
      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      


      

        <script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_allex_crc32_lib_crc32_esm_js-node_modules_github_mini-throttle_dist_deco-b38cad-fb30c470f64b.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/vendors-node_modules_github_clipboard-copy-element_dist_index_esm_js-node_modules_delegated-e-b37f7d-4db36910a4bc.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/app_assets_modules_github_command-palette_items_help-item_ts-app_assets_modules_github_comman-48ad9d-44cf245df946.js"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="https://github.githubassets.com/assets/command-palette-624c62d45c6c.js"></script>

            <header class="AppHeader">
    

    <div class="AppHeader-globalBar pb-2 js-global-bar">
      <div class="AppHeader-globalBar-start">
          <deferred-side-panel data-url="/_side-panels/global">
  <include-fragment data-target="deferred-side-panel.fragment">
      
  <button aria-label="Open global navigation menu" data-action="click:deferred-side-panel#loadPanel click:deferred-side-panel#panelOpened" data-show-dialog-id="dialog-ba59631b-199f-4e07-acfe-13956a650ade" id="dialog-show-dialog-ba59631b-199f-4e07-acfe-13956a650ade" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-bg-transparent p-0 color-fg-muted">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-three-bars Button-visual">
    <path d="M1 2.75A.75.75 0 0 1 1.75 2h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 2.75Zm0 5A.75.75 0 0 1 1.75 7h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 7.75ZM1.75 12h12.5a.75.75 0 0 1 0 1.5H1.75a.75.75 0 0 1 0-1.5Z"></path>
</svg>
</button>  

<div class="Overlay--hidden Overlay-backdrop--side Overlay-backdrop--placement-left" data-modal-dialog-overlay>
  <modal-dialog data-target="deferred-side-panel.panel" role="dialog" id="dialog-ba59631b-199f-4e07-acfe-13956a650ade" aria-modal="true" aria-disabled="true" aria-labelledby="dialog-ba59631b-199f-4e07-acfe-13956a650ade-title" aria-describedby="dialog-ba59631b-199f-4e07-acfe-13956a650ade-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-small-portrait Overlay--motion-scaleFade SidePanel">
    <div styles="flex-direction: row;" data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title sr-only" id="dialog-ba59631b-199f-4e07-acfe-13956a650ade-title">
        Global navigation
      </h1>
            <div data-view-component="true" class="d-flex">
      <div data-view-component="true" class="AppHeader-logo position-relative">
        <svg aria-hidden="true" height="24" viewBox="0 0 16 16" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
</div></div>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="dialog-ba59631b-199f-4e07-acfe-13956a650ade" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <div data-view-component="true" class="Overlay-body d-flex flex-column px-2">    <div data-view-component="true" class="d-flex flex-column mb-3">
        <nav aria-label="Site navigation" data-view-component="true" class="ActionList">
  
  <nav-list>
    <ul data-view-component="true" class="ActionListWrap">
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-hotkey="g d" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;HOME&quot;,&quot;label&quot;:null}" id="item-f98eb272-b09d-472c-81ce-c6c2b405543d" href="/dashboard" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-home">
    <path d="M6.906.664a1.749 1.749 0 0 1 2.187 0l5.25 4.2c.415.332.657.835.657 1.367v7.019A1.75 1.75 0 0 1 13.25 15h-3.5a.75.75 0 0 1-.75-.75V9H7v5.25a.75.75 0 0 1-.75.75h-3.5A1.75 1.75 0 0 1 1 13.25V6.23c0-.531.242-1.034.657-1.366l5.25-4.2Zm1.25 1.171a.25.25 0 0 0-.312 0l-5.25 4.2a.25.25 0 0 0-.094.196v7.019c0 .138.112.25.25.25H5.5V8.25a.75.75 0 0 1 .75-.75h3.5a.75.75 0 0 1 .75.75v5.25h2.75a.25.25 0 0 0 .25-.25V6.23a.25.25 0 0 0-.094-.195Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Home
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;ISSUES&quot;,&quot;label&quot;:null}" id="item-3defcfb9-97f8-4c5c-9a23-45e9971ee809" href="/issues" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PULL_REQUESTS&quot;,&quot;label&quot;:null}" id="item-a6173d34-24fd-4384-a9e7-dce560edda91" href="/pulls" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;DISCUSSIONS&quot;,&quot;label&quot;:null}" id="item-dd381879-f9d9-4481-b908-1fb17400f427" href="/discussions" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-comment-discussion">
    <path d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Discussions
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;CODESPACES&quot;,&quot;label&quot;:null}" id="item-6e84bee3-64a0-4cef-90b2-459f826dd052" href="https://github.com/codespaces" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-codespaces">
    <path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Codespaces
</span></a>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;EXPLORE&quot;,&quot;label&quot;:null}" id="item-be912d81-573c-49e6-9967-917c276964ec" href="/explore" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-telescope">
    <path d="M14.184 1.143v-.001l1.422 2.464a1.75 1.75 0 0 1-.757 2.451L3.104 11.713a1.75 1.75 0 0 1-2.275-.702l-.447-.775a1.75 1.75 0 0 1 .53-2.32L11.682.573a1.748 1.748 0 0 1 2.502.57Zm-4.709 9.32h-.001l2.644 3.863a.75.75 0 1 1-1.238.848l-1.881-2.75v2.826a.75.75 0 0 1-1.5 0v-2.826l-1.881 2.75a.75.75 0 1 1-1.238-.848l2.049-2.992a.746.746 0 0 1 .293-.253l1.809-.87a.749.749 0 0 1 .944.252ZM9.436 3.92h-.001l-4.97 3.39.942 1.63 5.42-2.61Zm3.091-2.108h.001l-1.85 1.26 1.505 2.605 2.016-.97a.247.247 0 0 0 .13-.151.247.247 0 0 0-.022-.199l-1.422-2.464a.253.253 0 0 0-.161-.119.254.254 0 0 0-.197.038ZM1.756 9.157a.25.25 0 0 0-.075.33l.447.775a.25.25 0 0 0 .325.1l1.598-.769-.83-1.436-1.465 1Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Explore
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;MARKETPLACE&quot;,&quot;label&quot;:null}" id="item-39bf6e1f-bcf3-4ff5-b3f7-5adb87bd0cba" href="/marketplace" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gift">
    <path d="M2 2.75A2.75 2.75 0 0 1 4.75 0c.983 0 1.873.42 2.57 1.232.268.318.497.668.68 1.042.183-.375.411-.725.68-1.044C9.376.42 10.266 0 11.25 0a2.75 2.75 0 0 1 2.45 4h.55c.966 0 1.75.784 1.75 1.75v2c0 .698-.409 1.301-1 1.582v4.918A1.75 1.75 0 0 1 13.25 16H2.75A1.75 1.75 0 0 1 1 14.25V9.332C.409 9.05 0 8.448 0 7.75v-2C0 4.784.784 4 1.75 4h.55c-.192-.375-.3-.8-.3-1.25ZM7.25 9.5H2.5v4.75c0 .138.112.25.25.25h4.5Zm1.5 0v5h4.5a.25.25 0 0 0 .25-.25V9.5Zm0-4V8h5.5a.25.25 0 0 0 .25-.25v-2a.25.25 0 0 0-.25-.25Zm-7 0a.25.25 0 0 0-.25.25v2c0 .138.112.25.25.25h5.5V5.5h-5.5Zm3-4a1.25 1.25 0 0 0 0 2.5h2.309c-.233-.818-.542-1.401-.878-1.793-.43-.502-.915-.707-1.431-.707ZM8.941 4h2.309a1.25 1.25 0 0 0 0-2.5c-.516 0-1 .205-1.43.707-.337.392-.646.975-.879 1.793Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Marketplace
</span></a>
  
  
</li>

</ul>  </nav-list>
</nav>

        <div data-view-component="true" class="my-3 d-flex flex-justify-center height-full">
          <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
</div>
</div>
      <div data-view-component="true" class="flex-1"></div>


      <div data-view-component="true" class="px-2">      <p class="color-fg-subtle text-small text-light">&copy; 2023 GitHub, Inc.</p>

      <div data-view-component="true" class="d-flex text-small text-light">
          <a target="_blank" href="/about" data-view-component="true" class="Link mr-2">About</a>
          <a target="_blank" href="https://github.blog" data-view-component="true" class="Link mr-2">Blog</a>
          <a target="_blank" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link mr-2">Terms</a>
          <a target="_blank" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link mr-2">Privacy</a>
          <a target="_blank" href="/security" data-view-component="true" class="Link mr-2">Security</a>
        <a target="_blank" href="https://www.githubstatus.com/" data-view-component="true" class="Link mr-3">Status</a>
</div></div>
</div>
      
</modal-dialog></div>

  </include-fragment>
</deferred-side-panel>

        <a
          class="AppHeader-logo ml-2"
          href="https://github.com/"
          data-hotkey="g d"
          aria-label="Homepage "
          data-turbo="false"
          data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;go to dashboard&quot;,&quot;label&quot;:&quot;icon:logo&quot;}"
        >
          <svg height="32" aria-hidden="true" viewBox="0 0 16 16" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github v-align-middle color-fg-default">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
        </a>

          <div class="AppHeader-context" >
  <div class="AppHeader-context-compact">
        <button aria-expanded="false" aria-haspopup="dialog" aria-label="Page context: twisted / twisted" id="dialog-show-context-region-dialog" data-show-dialog-id="context-region-dialog" type="button" data-view-component="true" class="AppHeader-context-compact-trigger Truncate Button--secondary Button--medium Button box-shadow-none">    <span class="Button-content">
      <span class="Button-label"><span class="AppHeader-context-compact-lead">
                <span class="AppHeader-context-compact-parentItem">twisted</span>
                <span class="no-wrap">&nbsp;/</span>

            </span>

            <strong class="AppHeader-context-compact-mainItem d-flex flex-items-center Truncate" >
  <span class="Truncate-text ">twisted</span>

</strong></span>
    </span>
</button>  

<div class="Overlay--hidden Overlay-backdrop--center" data-modal-dialog-overlay>
  <modal-dialog role="dialog" id="context-region-dialog" aria-modal="true" aria-disabled="true" aria-labelledby="context-region-dialog-title" aria-describedby="context-region-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="context-region-dialog-title">
        Navigate back to
      </h1>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="context-region-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <div data-view-component="true" class="Overlay-body">          <ul role="list" class="list-style-none" >
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;twisted&quot;,&quot;screen_size&quot;:&quot;compact&quot;}" href="/twisted" data-view-component="true" class="Link--primary Truncate d-flex flex-items-center py-1">
        <span class="AppHeader-context-item-label Truncate-text ">
            <svg aria-hidden="true" height="12" viewBox="0 0 16 16" version="1.1" width="12" data-view-component="true" class="octicon octicon-organization mr-1">
    <path d="M1.75 16A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0h8.5C11.216 0 12 .784 12 1.75v12.5c0 .085-.006.168-.018.25h2.268a.25.25 0 0 0 .25-.25V8.285a.25.25 0 0 0-.111-.208l-1.055-.703a.749.749 0 1 1 .832-1.248l1.055.703c.487.325.779.871.779 1.456v5.965A1.75 1.75 0 0 1 14.25 16h-3.5a.766.766 0 0 1-.197-.026c-.099.017-.2.026-.303.026h-3a.75.75 0 0 1-.75-.75V14h-1v1.25a.75.75 0 0 1-.75.75Zm-.25-1.75c0 .138.112.25.25.25H4v-1.25a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 .75.75v1.25h2.25a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25ZM3.75 6h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 3.75A.75.75 0 0 1 3.75 3h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 3.75Zm4 3A.75.75 0 0 1 7.75 6h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 7 6.75ZM7.75 3h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 9.75A.75.75 0 0 1 3.75 9h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 9.75ZM7.75 9h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5Z"></path>
</svg>

          twisted
        </span>

</a>
    </li>
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;twisted&quot;,&quot;screen_size&quot;:&quot;compact&quot;}" href="/twisted/twisted" data-view-component="true" class="Link--primary Truncate d-flex flex-items-center py-1">
        <span class="AppHeader-context-item-label Truncate-text ">
            <svg aria-hidden="true" height="12" viewBox="0 0 16 16" version="1.1" width="12" data-view-component="true" class="octicon octicon-repo mr-1">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>

          twisted
        </span>

</a>
    </li>
</ul>

</div>
      
</modal-dialog></div>
  </div>

  <div class="AppHeader-context-full">
    <nav role="navigation" aria-label="Page context">
      <ul role="list" class="list-style-none" >
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;twisted&quot;,&quot;screen_size&quot;:&quot;full&quot;}" data-hovercard-type="organization" data-hovercard-url="/orgs/twisted/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/twisted" data-view-component="true" class="AppHeader-context-item">
        <span class="AppHeader-context-item-label  ">

          twisted
        </span>

</a>
        <span class="AppHeader-context-item-separator">/</span>
    </li>
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;twisted&quot;,&quot;screen_size&quot;:&quot;full&quot;}" href="/twisted/twisted" data-view-component="true" class="AppHeader-context-item">
        <span class="AppHeader-context-item-label  ">

          twisted
        </span>

</a>
    </li>
</ul>

    </nav>
  </div>
</div>

      </div>
      <div class="AppHeader-globalBar-end">
          <div class="AppHeader-search" >
              


<qbsearch-input class="search-input" data-scope="repo:twisted/twisted" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="UHxTE4aQ49gUwF30xjcGnfOFJvPu3d3C0n-K_W0-CPM5lNzIYM7oRp2T-zvRkZP7Ew0KxsCtPbAyVexgsykpxg" data-max-custom-scopes="10" data-header-redesign-enabled="true" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="twisted/twisted" data-current-org="twisted" data-current-owner="" data-logged-in="true">
  <div
    class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center height-auto color-bg-transparent border-0 color-fg-subtle mx-0"
    data-action="click:qbsearch-input#searchInputContainerClicked"
  >
      
            <button type="button" data-action="click:qbsearch-input#handleExpand" class="AppHeader-button AppHeader-search-whenNarrow" aria-label="Search or jump to…" aria-expanded="false" aria-haspopup="dialog">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </button>


<div class="AppHeader-search-whenRegular">
  <div class="AppHeader-search-wrap AppHeader-search-wrap--hasTrailing">
    <div class="AppHeader-search-control">
      <label
        for="AppHeader-searchInput"
        aria-label="Search or jump to…"
        class="AppHeader-search-visual--leading"
      >
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
      </label>

                <button
            type="button"
            data-target="qbsearch-input.inputButton"
            data-action="click:qbsearch-input#handleExpand"
            class="AppHeader-searchButton form-control input-contrast text-left color-fg-subtle no-wrap"
            data-hotkey="s,/"
            data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;SEARCH&quot;,&quot;label&quot;:null}"
          >
            <div class="overflow-hidden">
              <span id="qb-input-query" data-target="qbsearch-input.inputButtonText">
                  Type <kbd class="AppHeader-search-kbd">/</kbd> to search
              </span>
            </div>
          </button>

    </div>


      <button type="button" id="AppHeader-commandPalette-button" class="AppHeader-search-action--trailing js-activate-command-palette" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;command_palette&quot;,&quot;label&quot;:&quot;open command palette&quot;}">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-command-palette">
    <path d="m6.354 8.04-4.773 4.773a.75.75 0 1 0 1.061 1.06L7.945 8.57a.75.75 0 0 0 0-1.06L2.642 2.206a.75.75 0 0 0-1.06 1.061L6.353 8.04ZM8.75 11.5a.75.75 0 0 0 0 1.5h5.5a.75.75 0 0 0 0-1.5h-5.5Z"></path>
</svg>
      </button>

      <tool-tip id="tooltip-a7b4abc8-3891-4eb9-8691-cf9a22746314" for="AppHeader-commandPalette-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Command palette</tool-tip>
  </div>
</div>

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay>
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-medium Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-absolute width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container"
          style="border-radius: 12px;"
          data-target="qbsearch-input.queryBuilderContainer"
          hidden
        >
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form id="query-builder-test-form" action="" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div
        class="QueryBuilder-StyledInput width-fit "
        data-target="query-builder.styledInput"
      >
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div
            aria-hidden="true"
            class="QueryBuilder-StyledInputContent"
            data-target="query-builder.styledInputContent"
          ></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-83982174-288b-4d02-9728-f5c931763b85" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" />
          </div>
        </div>
          <span class="sr-only" id="query-builder-test-clear">Clear</span>
          
  <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-target="query-builder.clearButton" data-action="
                click:query-builder#clear
                focus:query-builder#clearButtonFocus
                blur:query-builder#clearButtonBlur
              " variant="small" hidden="hidden" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>  

      </div>
      <template id="search-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
</template>

<template id="code-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</template>

<template id="file-code-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file-code">
    <path d="M4 1.75C4 .784 4.784 0 5.75 0h5.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v8.586A1.75 1.75 0 0 1 14.25 15h-9a.75.75 0 0 1 0-1.5h9a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 10 4.25V1.5H5.75a.25.25 0 0 0-.25.25v2.5a.75.75 0 0 1-1.5 0Zm1.72 4.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734l1.47-1.47-1.47-1.47a.75.75 0 0 1 0-1.06ZM3.28 7.78 1.81 9.25l1.47 1.47a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Zm8.22-6.218V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path>
</svg>
</template>

<template id="history-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-history">
    <path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path>
</svg>
</template>

<template id="repo-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
</template>

<template id="bookmark-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bookmark">
    <path d="M3 2.75C3 1.784 3.784 1 4.75 1h6.5c.966 0 1.75.784 1.75 1.75v11.5a.75.75 0 0 1-1.227.579L8 11.722l-3.773 3.107A.751.751 0 0 1 3 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v9.91l3.023-2.489a.75.75 0 0 1 .954 0l3.023 2.49V2.75a.25.25 0 0 0-.25-.25Z"></path>
</svg>
</template>

<template id="plus-circle-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus-circle">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm7.25-3.25v2.5h2.5a.75.75 0 0 1 0 1.5h-2.5v2.5a.75.75 0 0 1-1.5 0v-2.5h-2.5a.75.75 0 0 1 0-1.5h2.5v-2.5a.75.75 0 0 1 1.5 0Z"></path>
</svg>
</template>

<template id="circle-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-dot-fill">
    <path d="M8 4a4 4 0 1 1 0 8 4 4 0 0 1 0-8Z"></path>
</svg>
</template>

<template id="trash-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-trash">
    <path d="M11 1.75V3h2.25a.75.75 0 0 1 0 1.5H2.75a.75.75 0 0 1 0-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75ZM4.496 6.675l.66 6.6a.25.25 0 0 0 .249.225h5.19a.25.25 0 0 0 .249-.225l.66-6.6a.75.75 0 0 1 1.492.149l-.66 6.6A1.748 1.748 0 0 1 10.595 15h-5.19a1.75 1.75 0 0 1-1.741-1.575l-.66-6.6a.75.75 0 1 1 1.492-.15ZM6.5 1.75V3h3V1.75a.25.25 0 0 0-.25-.25h-2.5a.25.25 0 0 0-.25.25Z"></path>
</svg>
</template>

<template id="team-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-people">
    <path d="M2 5.5a3.5 3.5 0 1 1 5.898 2.549 5.508 5.508 0 0 1 3.034 4.084.75.75 0 1 1-1.482.235 4 4 0 0 0-7.9 0 .75.75 0 0 1-1.482-.236A5.507 5.507 0 0 1 3.102 8.05 3.493 3.493 0 0 1 2 5.5ZM11 4a3.001 3.001 0 0 1 2.22 5.018 5.01 5.01 0 0 1 2.56 3.012.749.749 0 0 1-.885.954.752.752 0 0 1-.549-.514 3.507 3.507 0 0 0-2.522-2.372.75.75 0 0 1-.574-.73v-.352a.75.75 0 0 1 .416-.672A1.5 1.5 0 0 0 11 5.5.75.75 0 0 1 11 4Zm-5.5-.5a2 2 0 1 0-.001 3.999A2 2 0 0 0 5.5 3.5Z"></path>
</svg>
</template>

<template id="project-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-project">
    <path d="M1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0ZM1.5 1.75v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25ZM11.75 3a.75.75 0 0 1 .75.75v7.5a.75.75 0 0 1-1.5 0v-7.5a.75.75 0 0 1 .75-.75Zm-8.25.75a.75.75 0 0 1 1.5 0v5.5a.75.75 0 0 1-1.5 0ZM8 3a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 3Z"></path>
</svg>
</template>

<template id="pencil-icon">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-pencil">
    <path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path>
</svg>
</template>

        <div class="position-relative">
                <ul
                  role="listbox"
                  class="ActionListWrap QueryBuilder-ListWrap"
                  aria-label="Suggestions"
                  data-action="
                    combobox-commit:query-builder#comboboxCommit
                    mousedown:query-builder#resultsMousedown
                  "
                  data-target="query-builder.resultsList"
                  data-persist-list=false
                  id="query-builder-test-results"
                ></ul>
        </div>
      <div class="FormControl-inlineValidation" id="validation-83982174-288b-4d02-9728-f5c931763b85" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only"></div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2">
              Search syntax tips
</a>            <div class="d-flex flex-1"></div>
                <button data-action="click:qbsearch-input#showFeedbackDialog" type="button" data-view-component="true" class="Button--link Button--medium Button color-fg-accent text-normal ml-2">    <span class="Button-content">
      <span class="Button-label">Give feedback</span>
    </span>
</button>  
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<div class="Overlay--hidden Overlay-backdrop--center" data-modal-dialog-overlay>
  <modal-dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" role="dialog" id="feedback-dialog" aria-modal="true" aria-disabled="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --></option></form><form id="code-search-feedback-form" data-turbo="false" action="/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="oRuzjQgwFRqCGikOuAcQ_d5qumIRlSO-NBibz8rmqmR2rQjHU50thKvJPJ9cL2OfblJU-GquHHf6k0fUpiv1DQ" />
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</modal-dialog></div>

    <custom-scopes data-target="qbsearch-input.customScopesManager">
    
<div class="Overlay--hidden Overlay-backdrop--center" data-modal-dialog-overlay>
  <modal-dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" role="dialog" id="custom-scopes-dialog" aria-modal="true" aria-disabled="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form id="custom-scopes-dialog-form" data-turbo="false" action="/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="0CRKFyDITU5i9jY0pPnrwKuKBSXGYTAbsQlDJtClA-JTnKzgyIlPAMNPIHBtWSYa7UKrkXF8UWkrlbDv5neZmg" />
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required>
              <input
                type="text"
                name="custom_scope_name"
                id="custom_scope_name"
                data-target="custom-scopes.customScopesNameField"
                class="form-control"
                autocomplete="off"
                placeholder="github-ruby"
                required
                maxlength="50">
              <input type="hidden" value="5yAOZN0-Ol7j3QgglEm6I2UjnTrTeFSUPhTCwcdt24wQRYnZBz10s__Sl-UqzWY2EhcRTTn9AYz6HJfCzzoN0w" data-csrf="true" />
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input
              type="text"
              name="custom_scope_query"
              id="custom_scope_query"
              data-target="custom-scopes.customScopesQueryField"
              class="form-control"
              autocomplete="off"
              placeholder="(repo:mona/a OR repo:mona/b) AND lang:python"
              required
              maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</modal-dialog></div>
    </custom-scopes>
  </div>
</qbsearch-input><input type="hidden" value="Pvvzc8ftSMjox8_oof343y3o3rp9G4STavLausMysKaOrulGEGg7--ny2nnF3iYcv6oLqo8U8A6NThnaBLdWTg" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf" />

          </div>

        <div class="AppHeader-actions position-relative">
          <action-menu data-select-variant="none" data-view-component="true">
  <focus-group direction="vertical" mnemonics retain>
    <div data-view-component="true" class="Button-withTooltip">  <button id="global-create-menu-button" popovertarget="global-create-menu-overlay" aria-label="Create something new" aria-controls="global-create-menu-list" aria-haspopup="true" type="button" data-view-component="true" class="AppHeader-button Button--secondary Button--small Button width-auto color-fg-muted">    <span class="Button-content">
        <span class="Button-visual Button-leadingVisual">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
        </span>
      <span class="Button-label"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg></span>
    </span>
</button>  <tool-tip id="tooltip-460fc9cd-8847-4b65-9a71-42b1548764ee" for="global-create-menu-button" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute">Create new...</tool-tip>
</div>

<anchored-position id="global-create-menu-overlay" anchor="global-create-menu-button" align="end" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      
        <div data-view-component="true">
  <ul aria-labelledby="global-create-menu-button" id="global-create-menu-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new repository&quot;}" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="/new" tabindex="-1" id="item-56a2c6e3-72e0-4362-ba9a-27ffd5ddedd8" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
              New repository

</span></a>
  
  
</li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;import repository&quot;}" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="/new/import" tabindex="-1" id="item-e6f39883-647d-4f0a-bd2b-fbdc718e369a" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-push">
    <path d="M1 2.5A2.5 2.5 0 0 1 3.5 0h8.75a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0V1.5h-8a1 1 0 0 0-1 1v6.708A2.493 2.493 0 0 1 3.5 9h3.25a.75.75 0 0 1 0 1.5H3.5a1 1 0 0 0 0 2h5.75a.75.75 0 0 1 0 1.5H3.5A2.5 2.5 0 0 1 1 11.5Zm13.23 7.79h-.001l-1.224-1.224v6.184a.75.75 0 0 1-1.5 0V9.066L10.28 10.29a.75.75 0 0 1-1.06-1.061l2.505-2.504a.75.75 0 0 1 1.06 0L15.29 9.23a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                Import repository

</span></a>
  
  
</li>
      <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new codespace&quot;}" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="/codespaces/new" tabindex="-1" id="item-09765897-1475-4104-8c09-153a18235dbe" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-codespaces">
    <path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                New codespace

</span></a>
  
  
</li>
      <li data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new gist&quot;}" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="https://gist.github.com/" tabindex="-1" id="item-7c6ce569-fccb-49b0-b4e3-ece38527e0da" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                New gist

</span></a>
  
  
</li>
      <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
      <li data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    <a href="/account/organizations/new" tabindex="-1" data-dont-follow-via-test="true" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;add_dropdown&quot;,&quot;label&quot;:&quot;new organization&quot;}" id="item-206a1fd6-89b4-469d-b9a2-d94b58ac3660" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-organization">
    <path d="M1.75 16A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0h8.5C11.216 0 12 .784 12 1.75v12.5c0 .085-.006.168-.018.25h2.268a.25.25 0 0 0 .25-.25V8.285a.25.25 0 0 0-.111-.208l-1.055-.703a.749.749 0 1 1 .832-1.248l1.055.703c.487.325.779.871.779 1.456v5.965A1.75 1.75 0 0 1 14.25 16h-3.5a.766.766 0 0 1-.197-.026c-.099.017-.2.026-.303.026h-3a.75.75 0 0 1-.75-.75V14h-1v1.25a.75.75 0 0 1-.75.75Zm-.25-1.75c0 .138.112.25.25.25H4v-1.25a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 .75.75v1.25h2.25a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25ZM3.75 6h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 3.75A.75.75 0 0 1 3.75 3h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 3.75Zm4 3A.75.75 0 0 1 7.75 6h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 7 6.75ZM7.75 3h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5ZM3 9.75A.75.75 0 0 1 3.75 9h.5a.75.75 0 0 1 0 1.5h-.5A.75.75 0 0 1 3 9.75ZM7.75 9h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1 0-1.5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
                New organization

</span></a>
  
  
</li>
</ul>  
</div>

</div></anchored-position>  </focus-group>
</action-menu>

          <div data-view-component="true" class="Button-withTooltip">
  <a href="/issues" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;ISSUES_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-e67dc8ae-2571-45bb-8f97-c07e9218e1e2" aria-labelledby="tooltip-8828ad54-32d8-41b7-9685-df0caf806d2a" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened Button-visual">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
</a>  <tool-tip id="tooltip-8828ad54-32d8-41b7-9685-df0caf806d2a" for="icon-button-e67dc8ae-2571-45bb-8f97-c07e9218e1e2" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Issues</tool-tip>
</div>
          <div data-view-component="true" class="Button-withTooltip">
  <a href="/pulls" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PULL_REQUESTS_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-650e9074-9fc6-48fe-8a97-75418ff6cb8c" aria-labelledby="tooltip-b487da50-fffc-4248-9c50-3975f74e4cee" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request Button-visual">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
</a>  <tool-tip id="tooltip-b487da50-fffc-4248-9c50-3975f74e4cee" for="icon-button-650e9074-9fc6-48fe-8a97-75418ff6cb8c" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Pull requests</tool-tip>
</div>

        </div>

        

<notification-indicator data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTY2MTA3NjgiLCJ0IjoxNjk4MTUyMDg4fQ==--471c4c45adbcb61ea0528b02d50aa5b7b78053fb010d3c0b0a55111cc4242187" data-indicator-mode="none" data-tooltip-global="You have unread notifications" data-tooltip-unavailable="Notifications are unavailable at the moment." data-tooltip-none="You have no unread notifications" data-header-redesign-enabled="true" data-fetch-indicator-src="/notifications/indicator" data-fetch-indicator-enabled="true" data-view-component="true" class="js-socket-channel">
  <a id="AppHeader-notifications-button" href="/notifications"
    class="AppHeader-button Button--secondary"

    style="width:32px;height:32px;"

    data-hotkey="g n"
    data-target="notification-indicator.link"
    aria-label="Notifications"

      data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;notifications&quot;,&quot;label&quot;:null}"
  >

    <span
      data-target="notification-indicator.badge"
      class="mail-status unread d-none" hidden>
    </span>

      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-inbox color-fg-muted mr-0">
    <path d="M2.8 2.06A1.75 1.75 0 0 1 4.41 1h7.18c.7 0 1.333.417 1.61 1.06l2.74 6.395c.04.093.06.194.06.295v4.5A1.75 1.75 0 0 1 14.25 15H1.75A1.75 1.75 0 0 1 0 13.25v-4.5c0-.101.02-.202.06-.295Zm1.61.44a.25.25 0 0 0-.23.152L1.887 8H4.75a.75.75 0 0 1 .6.3L6.625 10h2.75l1.275-1.7a.75.75 0 0 1 .6-.3h2.863L11.82 2.652a.25.25 0 0 0-.23-.152Zm10.09 7h-2.875l-1.275 1.7a.75.75 0 0 1-.6.3h-3.5a.75.75 0 0 1-.6-.3L4.375 9.5H1.5v3.75c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25Z"></path>
</svg>
  </a>

    <tool-tip data-target="notification-indicator.tooltip" id="tooltip-527e6944-02c9-4adc-a1a1-20b1eb4c0ab0" for="AppHeader-notifications-button" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute">Notifications</tool-tip>
</notification-indicator>

        

        <div class="AppHeader-user">
          <deferred-side-panel data-url="/_side-panels/user?memex_enabled=true&amp;repository=twisted&amp;user=AleksNeStu&amp;user_can_create_organizations=true&amp;user_id=16610768">
  <include-fragment data-target="deferred-side-panel.fragment">
      <user-drawer-side-panel>
      <button aria-label="Open user account menu" data-action="click:deferred-side-panel#loadPanel click:deferred-side-panel#panelOpened" data-show-dialog-id="dialog-78f431b2-975f-42cf-969e-945c9a5ccd14" id="dialog-show-dialog-78f431b2-975f-42cf-969e-945c9a5ccd14" type="button" data-view-component="true" class="AppHeader-logo Button--invisible Button--medium Button Button--invisible-noVisuals color-bg-transparent p-0">    <span class="Button-content">
      <span class="Button-label"><img src="https://avatars.githubusercontent.com/u/16610768?v=4" alt="" size="32" height="32" width="32" data-view-component="true" class="avatar circle" /></span>
    </span>
</button>  

<div class="Overlay--hidden Overlay-backdrop--side Overlay-backdrop--placement-right" data-modal-dialog-overlay>
  <modal-dialog data-target="deferred-side-panel.panel" role="dialog" id="dialog-78f431b2-975f-42cf-969e-945c9a5ccd14" aria-modal="true" aria-disabled="true" aria-labelledby="dialog-78f431b2-975f-42cf-969e-945c9a5ccd14-title" aria-describedby="dialog-78f431b2-975f-42cf-969e-945c9a5ccd14-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-small-portrait Overlay--motion-scaleFade SidePanel">
    <div styles="flex-direction: row;" data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title sr-only" id="dialog-78f431b2-975f-42cf-969e-945c9a5ccd14-title">
        Account menu
      </h1>
            <div data-view-component="true" class="d-flex">
      <div data-view-component="true" class="AppHeader-logo position-relative">
        <img src="https://avatars.githubusercontent.com/u/16610768?v=4" alt="" size="32" height="32" width="32" data-view-component="true" class="avatar circle" />
</div>        <div data-view-component="true" class="overflow-hidden d-flex width-full">        <div data-view-component="true" class="lh-condensed overflow-hidden d-flex flex-column flex-justify-center ml-2 f5 mr-auto width-full">
          <span data-view-component="true" class="Truncate text-bold">
    <span data-view-component="true" class="Truncate-text">
            AleksNeStu
</span>
</span>          <span data-view-component="true" class="Truncate color-fg-subtle">
    <span data-view-component="true" class="Truncate-text">
            Alex Nesterovich
</span>
</span></div>
</div>
</div>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="dialog-78f431b2-975f-42cf-969e-945c9a5ccd14" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
</div>
      <div data-view-component="true" class="Overlay-body d-flex flex-column px-2">    <div data-view-component="true" class="d-flex flex-column mb-3">
        <nav aria-label="User navigation" data-view-component="true" class="ActionList">
  
  <nav-list>
    <ul data-view-component="true" class="ActionListWrap">
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <button id="item-1d8ad45c-50e5-4ac3-89db-7e6cb26c8c36" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PROFILE&quot;,&quot;label&quot;:null}" id="item-51ad0696-6718-4f6e-9c66-fda39e8a5dda" href="https://github.com/AleksNeStu" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-person">
    <path d="M10.561 8.073a6.005 6.005 0 0 1 3.432 5.142.75.75 0 1 1-1.498.07 4.5 4.5 0 0 0-8.99 0 .75.75 0 0 1-1.498-.07 6.004 6.004 0 0 1 3.431-5.142 3.999 3.999 0 1 1 5.123 0ZM10.5 5a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your profile
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <button id="item-58152976-cca1-4605-85a9-192b12879078" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;YOUR_REPOSITORIES&quot;,&quot;label&quot;:null}" id="item-4a74aa2f-b235-46b1-b0f6-36ad5ad36068" href="/AleksNeStu?tab=repositories" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your repositories
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;YOUR_PROJECTS&quot;,&quot;label&quot;:null}" id="item-86aad993-31bc-4670-851b-32d02c3d5abe" href="/AleksNeStu?tab=projects" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-project">
    <path d="M1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0ZM1.5 1.75v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25ZM11.75 3a.75.75 0 0 1 .75.75v7.5a.75.75 0 0 1-1.5 0v-7.5a.75.75 0 0 1 .75-.75Zm-8.25.75a.75.75 0 0 1 1.5 0v5.5a.75.75 0 0 1-1.5 0ZM8 3a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 3Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your projects
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <button id="item-05f1690b-f476-4959-be67-b72ad4301004" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;YOUR_STARS&quot;,&quot;label&quot;:null}" id="item-9e69da82-84da-456b-8546-37ad0621e6f6" href="/AleksNeStu?tab=stars" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your stars
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;SPONSORS&quot;,&quot;label&quot;:null}" id="item-11275ef9-5c3e-4799-8da7-66098b289809" href="/sponsors/accounts" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-heart">
    <path d="m8 14.25.345.666a.75.75 0 0 1-.69 0l-.008-.004-.018-.01a7.152 7.152 0 0 1-.31-.17 22.055 22.055 0 0 1-3.434-2.414C2.045 10.731 0 8.35 0 5.5 0 2.836 2.086 1 4.25 1 5.797 1 7.153 1.802 8 3.02 8.847 1.802 10.203 1 11.75 1 13.914 1 16 2.836 16 5.5c0 2.85-2.045 5.231-3.885 6.818a22.066 22.066 0 0 1-3.744 2.584l-.018.01-.006.003h-.002ZM4.25 2.5c-1.336 0-2.75 1.164-2.75 3 0 2.15 1.58 4.144 3.365 5.682A20.58 20.58 0 0 0 8 13.393a20.58 20.58 0 0 0 3.135-2.211C12.92 9.644 14.5 7.65 14.5 5.5c0-1.836-1.414-3-2.75-3-1.373 0-2.609.986-3.029 2.456a.749.749 0 0 1-1.442 0C6.859 3.486 5.623 2.5 4.25 2.5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your sponsors
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;YOUR_GISTS&quot;,&quot;label&quot;:null}" id="item-788831ce-a0ec-42fa-bcb1-f8b2899e1ef9" href="https://gist.github.com/mine" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code-square">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25Zm7.47 3.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L10.69 8 9.22 6.53a.75.75 0 0 1 0-1.06ZM6.78 6.53 5.31 8l1.47 1.47a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Your gists
</span></a>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <button id="item-74b0d214-c5b3-485c-9fe4-832b2e795b5c" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <button id="item-c32c729e-01ef-4f3a-b29e-c03003e1c512" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <button id="item-48d1597b-ec49-4a05-864f-cf3c6603f546" type="button" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <span data-view-component="true" class="d-flex flex-items-center">    <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
</span>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          

  <span class="color-fg-muted">
    Loading...
  </span>

</span></button>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;SETTINGS&quot;,&quot;label&quot;:null}" id="item-5479b971-69f8-4979-b193-11e058abf722" href="/settings/profile" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gear">
    <path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Settings
</span></a>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;DOCS&quot;,&quot;label&quot;:null}" id="item-9c0cec86-c334-4059-b34e-be78c79ef9dd" href="https://docs.github.com" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-book">
    <path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          GitHub Docs
</span></a>
  
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;SUPPORT&quot;,&quot;label&quot;:null}" id="item-79fb7694-67bd-4ae2-b6b1-90df151980a4" href="https://support.github.com" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-people">
    <path d="M2 5.5a3.5 3.5 0 1 1 5.898 2.549 5.508 5.508 0 0 1 3.034 4.084.75.75 0 1 1-1.482.235 4 4 0 0 0-7.9 0 .75.75 0 0 1-1.482-.236A5.507 5.507 0 0 1 3.102 8.05 3.493 3.493 0 0 1 2 5.5ZM11 4a3.001 3.001 0 0 1 2.22 5.018 5.01 5.01 0 0 1 2.56 3.012.749.749 0 0 1-.885.954.752.752 0 0 1-.549-.514 3.507 3.507 0 0 0-2.522-2.372.75.75 0 0 1-.574-.73v-.352a.75.75 0 0 1 .416-.672A1.5 1.5 0 0 0 11 5.5.75.75 0 0 1 11 4Zm-5.5-.5a2 2 0 1 0-.001 3.999A2 2 0 0 0 5.5 3.5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          GitHub Support
</span></a>
  
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;LOGOUT&quot;,&quot;label&quot;:null}" id="item-93efd565-50ee-49ba-92c5-75c0be9ef964" href="/logout" data-view-component="true" class="ActionListContent">
      
        <span data-view-component="true" class="ActionListItem-label">
          Sign out
</span></a>
  
  
</li>

</ul>  </nav-list>
</nav>


</div>
</div>
      
</modal-dialog></div>
  </user-drawer-side-panel>

  </include-fragment>
</deferred-side-panel>
          
        </div>

        <div class="position-absolute mt-2">
            
<site-header-logged-in-user-menu>

</site-header-logged-in-user-menu>

        </div>
      </div>
    </div>


      <div class="AppHeader-localBar" >
        <nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav">

  <ul data-view-component="true" class="UnderlineNav-body list-style-none">
      <li data-view-component="true" class="d-inline-flex">
  <a id="code-tab" href="/twisted/twisted" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments repo_attestations /twisted/twisted" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g c" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Code&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        <span data-content="Code">Code</span>
          <span id="code-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="issues-tab" href="/twisted/twisted/issues" data-tab-item="i1issues-tab" data-selected-links="repo_issues repo_labels repo_milestones /twisted/twisted/issues" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Issues&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        <span data-content="Issues">Issues</span>
          <span id="issues-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="2,648" data-view-component="true" class="Counter">2.6k</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="/twisted/twisted/pulls" data-tab-item="i2pull-requests-tab" data-selected-links="repo_pulls checks /twisted/twisted/pulls" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Pull requests&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        <span data-content="Pull requests">Pull requests</span>
          <span id="pull-requests-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="117" data-view-component="true" class="Counter">117</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="/twisted/twisted/actions" data-tab-item="i3actions-tab" data-selected-links="repo_actions /twisted/twisted/actions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g a" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Actions&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        <span data-content="Actions">Actions</span>
          <span id="actions-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-tab" href="/twisted/twisted/security" data-tab-item="i4security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /twisted/twisted/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span data-content="Security">Security</span>
          <include-fragment src="/twisted/twisted/security/overall-count" accept="text/fragment+html"></include-fragment>

    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="insights-tab" href="/twisted/twisted/pulse" data-tab-item="i5insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /twisted/twisted/pulse" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Insights&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        <span data-content="Insights">Insights</span>
          <span id="insights-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">        <details data-view-component="true" class="details-overlay details-reset position-relative">
    <summary role="button" data-view-component="true">          <div class="UnderlineNav-item mr-0 border-0">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
            <span class="sr-only">More</span>
          </div>
</summary>
    <details-menu role="menu" data-view-component="true" class="dropdown-menu dropdown-menu-sw">
          <ul>
              <li data-menu-item="i0code-tab" hidden>
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments repo_attestations /twisted/twisted" href="/twisted/twisted">
                  Code
</a>              </li>
              <li data-menu-item="i1issues-tab" hidden>
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_issues repo_labels repo_milestones /twisted/twisted/issues" href="/twisted/twisted/issues">
                  Issues
</a>              </li>
              <li data-menu-item="i2pull-requests-tab" hidden>
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_pulls checks /twisted/twisted/pulls" href="/twisted/twisted/pulls">
                  Pull requests
</a>              </li>
              <li data-menu-item="i3actions-tab" hidden>
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_actions /twisted/twisted/actions" href="/twisted/twisted/actions">
                  Actions
</a>              </li>
              <li data-menu-item="i4security-tab" hidden>
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="security overview alerts policy token_scanning code_scanning /twisted/twisted/security" href="/twisted/twisted/security">
                  Security
</a>              </li>
              <li data-menu-item="i5insights-tab" hidden>
                <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /twisted/twisted/pulse" href="/twisted/twisted/pulse">
                  Insights
</a>              </li>
          </ul>
</details-menu>
</details></div>
</nav>
      </div>
</header>


      <div hidden="hidden" data-view-component="true" class="js-stale-session-flash stale-session-flash flash flash-warn mb-3">
  
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span class="js-stale-session-flash-signed-in" hidden>You signed in with another tab or window. <a class="Link--inTextBlock" href="">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-signed-out" hidden>You signed out in another tab or window. <a class="Link--inTextBlock" href="">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-switched" hidden>You switched accounts on another tab or window. <a class="Link--inTextBlock" href="">Reload</a> to refresh your session.</span>

    <div data-view-component="true" class="flash-close">
  <button id="icon-button-66e75080-306f-4aa6-8cc5-8de2201da857" aria-labelledby="tooltip-49accd94-4fb9-4fb1-aef5-7ee38ce93f55" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium js-flash-close">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button>  <tool-tip id="tooltip-49accd94-4fb9-4fb1-aef5-7ee38ce93f55" for="icon-button-66e75080-306f-4aa6-8cc5-8de2201da857" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Dismiss alert</tool-tip>
</div>

  
</div>
          
    </div>

  <div id="start-of-content" class="show-on-focus"></div>








    <div id="js-flash-container" data-turbo-replace>





  <template class="js-flash-template">
    
<div class="flash flash-full   {{ className }}">
  <div class="px-2" >
    <button autofocus class="flash-close js-flash-close" type="button" aria-label="Dismiss this message">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    <div aria-atomic="true" role="alert" class="js-flash-alert">
      
      <div>{{ message }}</div>

    </div>
  </div>
</div>
  </template>
</div>


    
    <notification-shelf-watcher data-base-url="https://github.com/notifications/beta/shelf" data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTY2MTA3NjgiLCJ0IjoxNjk4MTUyMDg5fQ==--8db8ff9fd44392358bd06233f859988fd1841d81b94db72e9b7ff1ed5b5cac69" data-view-component="true" class="js-socket-channel"></notification-shelf-watcher>
  <div hidden data-initial data-target="notification-shelf-watcher.placeholder"></div>






      <details
  class="details-reset details-overlay details-overlay-dark js-command-palette-dialog"
  id="command-palette-pjax-container"
  data-turbo-replace
>
  <summary aria-label="Command palette trigger" tabindex="-1"></summary>
  <details-dialog class="command-palette-details-dialog d-flex flex-column flex-justify-center height-fit" aria-label="Command palette">
    <command-palette
      class="command-palette color-bg-default rounded-3 border color-shadow-small"
      return-to=/twisted/twisted/blob/trunk/README.rst
      user-id="16610768"
      activation-hotkey="Mod+k,Mod+Alt+k"
      command-mode-hotkey="Mod+Shift+k"
      data-action="
        command-palette-input-ready:command-palette#inputReady
        command-palette-page-stack-updated:command-palette#updateInputScope
        itemsUpdated:command-palette#itemsUpdated
        keydown:command-palette#onKeydown
        loadingStateChanged:command-palette#loadingStateChanged
        selectedItemChanged:command-palette#selectedItemChanged
        pageFetchError:command-palette#pageFetchError
      ">

        <command-palette-mode
          data-char="#"
            data-scope-types="[&quot;&quot;]"
            data-placeholder="Search issues and pull requests"
        ></command-palette-mode>
        <command-palette-mode
          data-char="#"
            data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
            data-placeholder="Search issues, pull requests, discussions, and projects"
        ></command-palette-mode>
        <command-palette-mode
          data-char="!"
            data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
            data-placeholder="Search projects"
        ></command-palette-mode>
        <command-palette-mode
          data-char="@"
            data-scope-types="[&quot;&quot;]"
            data-placeholder="Search or jump to a user, organization, or repository"
        ></command-palette-mode>
        <command-palette-mode
          data-char="@"
            data-scope-types="[&quot;owner&quot;]"
            data-placeholder="Search or jump to a repository"
        ></command-palette-mode>
        <command-palette-mode
          data-char="/"
            data-scope-types="[&quot;repository&quot;]"
            data-placeholder="Search files"
        ></command-palette-mode>
        <command-palette-mode
          data-char="?"
        ></command-palette-mode>
        <command-palette-mode
          data-char="&gt;"
            data-placeholder="Run a command"
        ></command-palette-mode>
        <command-palette-mode
          data-char=""
            data-scope-types="[&quot;&quot;]"
            data-placeholder="Search or jump to..."
        ></command-palette-mode>
        <command-palette-mode
          data-char=""
            data-scope-types="[&quot;owner&quot;]"
            data-placeholder="Search or jump to..."
        ></command-palette-mode>
      <command-palette-mode
        class="js-command-palette-default-mode"
        data-char=""
        data-placeholder="Search or jump to..."
      ></command-palette-mode>

      <command-palette-input placeholder="Search or jump to..."

        data-action="
          command-palette-input:command-palette#onInput
          command-palette-select:command-palette#onSelect
          command-palette-descope:command-palette#onDescope
          command-palette-cleared:command-palette#onInputClear
        "
      >
        <div class="js-search-icon d-flex flex-items-center mr-2" style="height: 26px">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search color-fg-muted">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
        </div>
        <div class="js-spinner d-flex flex-items-center mr-2 color-fg-muted" hidden>
          <svg aria-label="Loading" class="anim-rotate" viewBox="0 0 16 16" fill="none" width="16" height="16">
            <circle
              cx="8"
              cy="8"
              r="7"
              stroke="currentColor"
              stroke-opacity="0.25"
              stroke-width="2"
              vector-effect="non-scaling-stroke"
            ></circle>
            <path
              d="M15 8a7.002 7.002 0 00-7-7"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              vector-effect="non-scaling-stroke"
            ></path>
          </svg>
        </div>
        <command-palette-scope >
          <div data-target="command-palette-scope.placeholder" hidden class="color-fg-subtle">/&nbsp;&nbsp;<span class="text-semibold color-fg-default">...</span>&nbsp;&nbsp;/&nbsp;&nbsp;</div>
              <command-palette-token
                data-text="twisted"
                data-id="MDEyOk9yZ2FuaXphdGlvbjcxNjU0Ng=="
                data-type="owner"
                data-value="twisted"
                data-targets="command-palette-scope.tokens"
                class="color-fg-default text-semibold"
                style="white-space:nowrap;line-height:20px;"
                >twisted<span class="color-fg-subtle text-normal">&nbsp;&nbsp;/&nbsp;&nbsp;</span></command-palette-token>
              <command-palette-token
                data-text="twisted"
                data-id="MDEwOlJlcG9zaXRvcnkxOTg1MzU4"
                data-type="repository"
                data-value="twisted"
                data-targets="command-palette-scope.tokens"
                class="color-fg-default text-semibold"
                style="white-space:nowrap;line-height:20px;"
                >twisted<span class="color-fg-subtle text-normal">&nbsp;&nbsp;/&nbsp;&nbsp;</span></command-palette-token>
        </command-palette-scope>
        <div class="command-palette-input-group flex-1 form-control border-0 box-shadow-none" style="z-index: 0">
          <div class="command-palette-typeahead position-absolute d-flex flex-items-center Truncate">
            <span class="typeahead-segment input-mirror" data-target="command-palette-input.mirror"></span>
            <span class="Truncate-text" data-target="command-palette-input.typeaheadText"></span>
            <span class="typeahead-segment" data-target="command-palette-input.typeaheadPlaceholder"></span>
          </div>
          <input
            class="js-overlay-input typeahead-input d-none"
            disabled
            tabindex="-1"
            aria-label="Hidden input for typeahead"
          >
          <input
            type="text"
            autocomplete="off"
            autocorrect="off"
            autocapitalize="off"
            spellcheck="false"
            class="js-input typeahead-input form-control border-0 box-shadow-none input-block width-full no-focus-indicator"
            aria-label="Command palette input"
            aria-haspopup="listbox"
            aria-expanded="false"
            aria-autocomplete="list"
            aria-controls="command-palette-page-stack"
            role="combobox"
            data-action="
              input:command-palette-input#onInput
              keydown:command-palette-input#onKeydown
            "
          >
        </div>
          <div data-view-component="true" class="position-relative d-inline-block">
    <button aria-keyshortcuts="Control+Backspace" data-action="click:command-palette-input#onClear keypress:command-palette-input#onClear" data-target="command-palette-input.clearButton" id="command-palette-clear-button" hidden="hidden" type="button" data-view-component="true" class="btn-octicon command-palette-input-clear-button">      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>    <tool-tip id="tooltip-45bb391a-c30c-40b0-b6a0-a78b83c4eee4" for="command-palette-clear-button" popover="manual" data-direction="w" data-type="label" data-view-component="true" class="sr-only position-absolute">Clear Command Palette</tool-tip>
</div>
      </command-palette-input>

      <command-palette-page-stack
        data-default-scope-id="MDEwOlJlcG9zaXRvcnkxOTg1MzU4"
        data-default-scope-type="Repository"
        data-action="command-palette-page-octicons-cached:command-palette-page-stack#cacheOcticons"
      >
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
            data-mode=""
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">#</kbd> to search pull requests
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
            data-mode=""
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">#</kbd> to search issues
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
            data-mode=""
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">#</kbd> to search discussions
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
            data-mode=""
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">!</kbd> to search projects
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;owner&quot;]"
            data-mode=""
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">@</kbd> to search teams
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;]"
            data-mode=""
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">@</kbd> to search people and organizations
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
            data-mode=""
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type <kbd class="hx_kbd">&gt;</kbd> to activate command mode
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
            data-mode=""
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Go to your accessibility settings to change your keyboard shortcuts
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
            data-mode="#"
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type author:@me to search your content
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
            data-mode="#"
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:pr to filter to pull requests
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
            data-mode="#"
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:issue to filter to issues
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
            data-mode="#"
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:project to filter to projects
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
          <command-palette-tip
            class="color-fg-muted f6 px-3 py-1 my-2"
              data-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
            data-mode="#"
            data-value="">
            <div class="d-flex flex-items-start flex-justify-between">
              <div>
                <span class="text-bold">Tip:</span>
                  Type is:open to filter to open content
              </div>
              <div class="ml-2 flex-shrink-0">
                Type <kbd class="hx_kbd">?</kbd> for help and tips
              </div>
            </div>
          </command-palette-tip>
        <command-palette-tip class="mx-3 my-2 flash flash-error d-flex flex-items-center" data-scope-types="*" data-on-error>
          <div>
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
          </div>
          <div class="px-2">
            We’ve encountered an error and some results aren't available at this time. Type a new search or try again later.
          </div>
        </command-palette-tip>
        <command-palette-tip class="h4 color-fg-default pl-3 pb-2 pt-3" data-on-empty data-scope-types="*" data-match-mode="[^?]|^$">
          No results matched your search
        </command-palette-tip>

        <div hidden>

            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="arrow-right-color-fg-muted">
              <svg height="16" class="octicon octicon-arrow-right color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8.22 2.97a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l2.97-2.97H3.75a.75.75 0 0 1 0-1.5h7.44L8.22 4.03a.75.75 0 0 1 0-1.06Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="arrow-right-color-fg-default">
              <svg height="16" class="octicon octicon-arrow-right color-fg-default" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8.22 2.97a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l2.97-2.97H3.75a.75.75 0 0 1 0-1.5h7.44L8.22 4.03a.75.75 0 0 1 0-1.06Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="codespaces-color-fg-muted">
              <svg height="16" class="octicon octicon-codespaces color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="copy-color-fg-muted">
              <svg height="16" class="octicon octicon-copy color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="dash-color-fg-muted">
              <svg height="16" class="octicon octicon-dash color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M2 7.75A.75.75 0 0 1 2.75 7h10a.75.75 0 0 1 0 1.5h-10A.75.75 0 0 1 2 7.75Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="file-color-fg-muted">
              <svg height="16" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="gear-color-fg-muted">
              <svg height="16" class="octicon octicon-gear color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="lock-color-fg-muted">
              <svg height="16" class="octicon octicon-lock color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M4 4a4 4 0 0 1 8 0v2h.25c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 12.25 15h-8.5A1.75 1.75 0 0 1 2 13.25v-5.5C2 6.784 2.784 6 3.75 6H4Zm8.25 3.5h-8.5a.25.25 0 0 0-.25.25v5.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25ZM10.5 6V4a2.5 2.5 0 1 0-5 0v2Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="moon-color-fg-muted">
              <svg height="16" class="octicon octicon-moon color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M9.598 1.591a.749.749 0 0 1 .785-.175 7.001 7.001 0 1 1-8.967 8.967.75.75 0 0 1 .961-.96 5.5 5.5 0 0 0 7.046-7.046.75.75 0 0 1 .175-.786Zm1.616 1.945a7 7 0 0 1-7.678 7.678 5.499 5.499 0 1 0 7.678-7.678Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="person-color-fg-muted">
              <svg height="16" class="octicon octicon-person color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M10.561 8.073a6.005 6.005 0 0 1 3.432 5.142.75.75 0 1 1-1.498.07 4.5 4.5 0 0 0-8.99 0 .75.75 0 0 1-1.498-.07 6.004 6.004 0 0 1 3.431-5.142 3.999 3.999 0 1 1 5.123 0ZM10.5 5a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="pencil-color-fg-muted">
              <svg height="16" class="octicon octicon-pencil color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="issue-opened-open">
              <svg height="16" class="octicon octicon-issue-opened open" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="git-pull-request-draft-color-fg-muted">
              <svg height="16" class="octicon octicon-git-pull-request-draft color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M3.25 1A2.25 2.25 0 0 1 4 5.372v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.251 2.251 0 0 1 3.25 1Zm9.5 14a2.25 2.25 0 1 1 0-4.5 2.25 2.25 0 0 1 0 4.5ZM2.5 3.25a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0ZM3.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm9.5 0a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM14 7.5a1.25 1.25 0 1 1-2.5 0 1.25 1.25 0 0 1 2.5 0Zm0-4.25a1.25 1.25 0 1 1-2.5 0 1.25 1.25 0 0 1 2.5 0Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="search-color-fg-muted">
              <svg height="16" class="octicon octicon-search color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="sun-color-fg-muted">
              <svg height="16" class="octicon octicon-sun color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 12a4 4 0 1 1 0-8 4 4 0 0 1 0 8Zm0-1.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5Zm5.657-8.157a.75.75 0 0 1 0 1.061l-1.061 1.06a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734l1.06-1.06a.75.75 0 0 1 1.06 0Zm-9.193 9.193a.75.75 0 0 1 0 1.06l-1.06 1.061a.75.75 0 1 1-1.061-1.06l1.06-1.061a.75.75 0 0 1 1.061 0ZM8 0a.75.75 0 0 1 .75.75v1.5a.75.75 0 0 1-1.5 0V.75A.75.75 0 0 1 8 0ZM3 8a.75.75 0 0 1-.75.75H.75a.75.75 0 0 1 0-1.5h1.5A.75.75 0 0 1 3 8Zm13 0a.75.75 0 0 1-.75.75h-1.5a.75.75 0 0 1 0-1.5h1.5A.75.75 0 0 1 16 8Zm-8 5a.75.75 0 0 1 .75.75v1.5a.75.75 0 0 1-1.5 0v-1.5A.75.75 0 0 1 8 13Zm3.536-1.464a.75.75 0 0 1 1.06 0l1.061 1.06a.75.75 0 0 1-1.06 1.061l-1.061-1.06a.75.75 0 0 1 0-1.061ZM2.343 2.343a.75.75 0 0 1 1.061 0l1.06 1.061a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018l-1.06-1.06a.75.75 0 0 1 0-1.06Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="sync-color-fg-muted">
              <svg height="16" class="octicon octicon-sync color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M1.705 8.005a.75.75 0 0 1 .834.656 5.5 5.5 0 0 0 9.592 2.97l-1.204-1.204a.25.25 0 0 1 .177-.427h3.646a.25.25 0 0 1 .25.25v3.646a.25.25 0 0 1-.427.177l-1.38-1.38A7.002 7.002 0 0 1 1.05 8.84a.75.75 0 0 1 .656-.834ZM8 2.5a5.487 5.487 0 0 0-4.131 1.869l1.204 1.204A.25.25 0 0 1 4.896 6H1.25A.25.25 0 0 1 1 5.75V2.104a.25.25 0 0 1 .427-.177l1.38 1.38A7.002 7.002 0 0 1 14.95 7.16a.75.75 0 0 1-1.49.178A5.5 5.5 0 0 0 8 2.5Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="trash-color-fg-muted">
              <svg height="16" class="octicon octicon-trash color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M11 1.75V3h2.25a.75.75 0 0 1 0 1.5H2.75a.75.75 0 0 1 0-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75ZM4.496 6.675l.66 6.6a.25.25 0 0 0 .249.225h5.19a.25.25 0 0 0 .249-.225l.66-6.6a.75.75 0 0 1 1.492.149l-.66 6.6A1.748 1.748 0 0 1 10.595 15h-5.19a1.75 1.75 0 0 1-1.741-1.575l-.66-6.6a.75.75 0 1 1 1.492-.15ZM6.5 1.75V3h3V1.75a.25.25 0 0 0-.25-.25h-2.5a.25.25 0 0 0-.25.25Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="key-color-fg-muted">
              <svg height="16" class="octicon octicon-key color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M10.5 0a5.499 5.499 0 1 1-1.288 10.848l-.932.932a.749.749 0 0 1-.53.22H7v.75a.749.749 0 0 1-.22.53l-.5.5a.749.749 0 0 1-.53.22H5v.75a.749.749 0 0 1-.22.53l-.5.5a.749.749 0 0 1-.53.22h-2A1.75 1.75 0 0 1 0 14.25v-2c0-.199.079-.389.22-.53l4.932-4.932A5.5 5.5 0 0 1 10.5 0Zm-4 5.5c-.001.431.069.86.205 1.269a.75.75 0 0 1-.181.768L1.5 12.56v1.69c0 .138.112.25.25.25h1.69l.06-.06v-1.19a.75.75 0 0 1 .75-.75h1.19l.06-.06v-1.19a.75.75 0 0 1 .75-.75h1.19l1.023-1.025a.75.75 0 0 1 .768-.18A4 4 0 1 0 6.5 5.5ZM11 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="comment-discussion-color-fg-muted">
              <svg height="16" class="octicon octicon-comment-discussion color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="bell-color-fg-muted">
              <svg height="16" class="octicon octicon-bell color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 16a2 2 0 0 0 1.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 0 0 8 16ZM3 5a5 5 0 0 1 10 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.519 1.519 0 0 1 13.482 13H2.518a1.516 1.516 0 0 1-1.263-2.36l1.703-2.554A.255.255 0 0 0 3 7.947Zm5-3.5A3.5 3.5 0 0 0 4.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.017.017 0 0 0-.003.01l.001.006c0 .002.002.004.004.006l.006.004.007.001h10.964l.007-.001.006-.004.004-.006.001-.007a.017.017 0 0 0-.003-.01l-1.703-2.554a1.745 1.745 0 0 1-.294-.97V5A3.5 3.5 0 0 0 8 1.5Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="bell-slash-color-fg-muted">
              <svg height="16" class="octicon octicon-bell-slash color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="m4.182 4.31.016.011 10.104 7.316.013.01 1.375.996a.75.75 0 1 1-.88 1.214L13.626 13H2.518a1.516 1.516 0 0 1-1.263-2.36l1.703-2.554A.255.255 0 0 0 3 7.947V5.305L.31 3.357a.75.75 0 1 1 .88-1.214Zm7.373 7.19L4.5 6.391v1.556c0 .346-.102.683-.294.97l-1.703 2.556a.017.017 0 0 0-.003.01c0 .005.002.009.005.012l.006.004.007.001ZM8 1.5c-.997 0-1.895.416-2.534 1.086A.75.75 0 1 1 4.38 1.55 5 5 0 0 1 13 5v2.373a.75.75 0 0 1-1.5 0V5A3.5 3.5 0 0 0 8 1.5ZM8 16a2 2 0 0 1-1.985-1.75c-.017-.137.097-.25.235-.25h3.5c.138 0 .252.113.235.25A2 2 0 0 1 8 16Z"></path></svg>
            </div>
            <div data-targets="command-palette-page-stack.localOcticons" data-octicon-id="paintbrush-color-fg-muted">
              <svg height="16" class="octicon octicon-paintbrush color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M11.134 1.535c.7-.509 1.416-.942 2.076-1.155.649-.21 1.463-.267 2.069.34.603.601.568 1.411.368 2.07-.202.668-.624 1.39-1.125 2.096-1.011 1.424-2.496 2.987-3.775 4.249-1.098 1.084-2.132 1.839-3.04 2.3a3.744 3.744 0 0 1-1.055 3.217c-.431.431-1.065.691-1.657.861-.614.177-1.294.287-1.914.357A21.151 21.151 0 0 1 .797 16H.743l.007-.75H.749L.742 16a.75.75 0 0 1-.743-.742l.743-.008-.742.007v-.054a21.25 21.25 0 0 1 .13-2.284c.067-.647.187-1.287.358-1.914.17-.591.43-1.226.86-1.657a3.746 3.746 0 0 1 3.227-1.054c.466-.893 1.225-1.907 2.314-2.982 1.271-1.255 2.833-2.75 4.245-3.777ZM1.62 13.089c-.051.464-.086.929-.104 1.395.466-.018.932-.053 1.396-.104a10.511 10.511 0 0 0 1.668-.309c.526-.151.856-.325 1.011-.48a2.25 2.25 0 1 0-3.182-3.182c-.155.155-.329.485-.48 1.01a10.515 10.515 0 0 0-.309 1.67Zm10.396-10.34c-1.224.89-2.605 2.189-3.822 3.384l1.718 1.718c1.21-1.205 2.51-2.597 3.387-3.833.47-.662.78-1.227.912-1.662.134-.444.032-.551.009-.575h-.001V1.78c-.014-.014-.113-.113-.548.027-.432.14-.995.462-1.655.942Zm-4.832 7.266-.001.001a9.859 9.859 0 0 0 1.63-1.142L7.155 7.216a9.7 9.7 0 0 0-1.161 1.607c.482.302.889.71 1.19 1.192Z"></path></svg>
            </div>

            <command-palette-item-group
              data-group-id="top"
              data-group-title="Top result"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="0"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="commands"
              data-group-title="Commands"
              data-group-hint="Type &gt; to filter"
              data-group-limits="{&quot;static_items_page&quot;:50,&quot;issue&quot;:50,&quot;pull_request&quot;:50,&quot;discussion&quot;:50}"
              data-default-priority="1"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="global_commands"
              data-group-title="Global Commands"
              data-group-hint="Type &gt; to filter"
              data-group-limits="{&quot;issue&quot;:0,&quot;pull_request&quot;:0,&quot;discussion&quot;:0}"
              data-default-priority="2"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="this_page"
              data-group-title="This Page"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="3"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="files"
              data-group-title="Files"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="4"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="default"
              data-group-title="Default"
              data-group-hint=""
              data-group-limits="{&quot;static_items_page&quot;:50}"
              data-default-priority="5"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="pages"
              data-group-title="Pages"
              data-group-hint=""
              data-group-limits="{&quot;repository&quot;:10}"
              data-default-priority="6"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="access_policies"
              data-group-title="Access Policies"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="7"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="organizations"
              data-group-title="Organizations"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="8"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="repositories"
              data-group-title="Repositories"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="9"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="references"
              data-group-title="Issues, pull requests, and discussions"
              data-group-hint="Type # to filter"
              data-group-limits="{}"
              data-default-priority="10"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="teams"
              data-group-title="Teams"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="11"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="users"
              data-group-title="Users"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="12"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="memex_projects"
              data-group-title="Projects"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="13"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="projects"
              data-group-title="Projects (classic)"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="14"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="footer"
              data-group-title="Footer"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="15"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="modes_help"
              data-group-title="Modes"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="16"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="filters_help"
              data-group-title="Use filters in issues, pull requests, discussions, and projects"
              data-group-hint=""
              data-group-limits="{}"
              data-default-priority="17"
            >
            </command-palette-item-group>

            <command-palette-page
              data-page-title="twisted"
              data-scope-id="MDEyOk9yZ2FuaXphdGlvbjcxNjU0Ng=="
              data-scope-type="owner"
              data-targets="command-palette-page-stack.defaultPages"
              hidden
            >
            </command-palette-page>
            <command-palette-page
              data-page-title="twisted"
              data-scope-id="MDEwOlJlcG9zaXRvcnkxOTg1MzU4"
              data-scope-type="repository"
              data-targets="command-palette-page-stack.defaultPages"
              hidden
            >
            </command-palette-page>
        </div>

        <command-palette-page data-is-root>
        </command-palette-page>
          <command-palette-page
            data-page-title="twisted"
            data-scope-id="MDEyOk9yZ2FuaXphdGlvbjcxNjU0Ng=="
            data-scope-type="owner"
          >
          </command-palette-page>
          <command-palette-page
            data-page-title="twisted"
            data-scope-id="MDEwOlJlcG9zaXRvcnkxOTg1MzU4"
            data-scope-type="repository"
          >
          </command-palette-page>
      </command-palette-page-stack>

      <server-defined-provider data-type="search-links" data-targets="command-palette.serverDefinedProviderElements"></server-defined-provider>
      <server-defined-provider data-type="help" data-targets="command-palette.serverDefinedProviderElements">
          <command-palette-help
            data-group="modes_help"
              data-prefix="#"
              data-scope-types="[&quot;&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Search for <strong>issues</strong> and <strong>pull requests</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">#</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="modes_help"
              data-prefix="#"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Search for <strong>issues, pull requests, discussions,</strong> and <strong>projects</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">#</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="modes_help"
              data-prefix="@"
              data-scope-types="[&quot;&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Search for <strong>organizations, repositories,</strong> and <strong>users</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">@</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="modes_help"
              data-prefix="!"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Search for <strong>projects</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">!</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="modes_help"
              data-prefix="/"
              data-scope-types="[&quot;repository&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Search for <strong>files</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">/</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="modes_help"
              data-prefix="&gt;"
          >
            <span data-target="command-palette-help.titleElement">Activate <strong>command mode</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">&gt;</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# author:@me"
          >
            <span data-target="command-palette-help.titleElement">Search your issues, pull requests, and discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># author:@me</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# author:@me"
          >
            <span data-target="command-palette-help.titleElement">Search your issues, pull requests, and discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># author:@me</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# is:pr"
          >
            <span data-target="command-palette-help.titleElement">Filter to pull requests</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:pr</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# is:issue"
          >
            <span data-target="command-palette-help.titleElement">Filter to issues</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:issue</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# is:discussion"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Filter to discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:discussion</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# is:project"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Filter to projects</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:project</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# is:open"
          >
            <span data-target="command-palette-help.titleElement">Filter to open issues, pull requests, and discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:open</kbd>
              </span>
          </command-palette-help>
      </server-defined-provider>

        <server-defined-provider
          data-type="commands"
          data-fetch-debounce="0"
            data-src="/command_palette/commands"
          data-supported-modes="[]"
            data-supports-commands
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="prefetched"
          data-fetch-debounce="0"
            data-src="/command_palette/jump_to_page_navigation"
          data-supported-modes="[&quot;&quot;]"
            data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;,&quot;repository&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/issues"
          data-supported-modes="[&quot;#&quot;,&quot;#&quot;]"
            data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;,&quot;&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/jump_to"
          data-supported-modes="[&quot;@&quot;,&quot;@&quot;]"
            data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/jump_to_members_only"
          data-supported-modes="[&quot;@&quot;,&quot;@&quot;,&quot;&quot;,&quot;&quot;]"
            data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="prefetched"
          data-fetch-debounce="0"
            data-src="/command_palette/jump_to_members_only_prefetched"
          data-supported-modes="[&quot;@&quot;,&quot;@&quot;,&quot;&quot;,&quot;&quot;]"
            data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="files"
          data-fetch-debounce="0"
            data-src="/command_palette/files"
          data-supported-modes="[&quot;/&quot;]"
            data-supported-scope-types="[&quot;repository&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/discussions"
          data-supported-modes="[&quot;#&quot;]"
            data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/projects"
          data-supported-modes="[&quot;#&quot;,&quot;!&quot;]"
            data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="prefetched"
          data-fetch-debounce="0"
            data-src="/command_palette/recent_issues"
          data-supported-modes="[&quot;#&quot;,&quot;#&quot;]"
            data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;,&quot;&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/teams"
          data-supported-modes="[&quot;@&quot;,&quot;&quot;]"
            data-supported-scope-types="[&quot;owner&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/name_with_owner_repository"
          data-supported-modes="[&quot;@&quot;,&quot;@&quot;,&quot;&quot;,&quot;&quot;]"
            data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]"
          
          data-targets="command-palette.serverDefinedProviderElements"
          ></server-defined-provider>
    </command-palette>
  </details-dialog>
</details>

<div class="position-fixed bottom-0 left-0 ml-5 mb-5 js-command-palette-toasts" style="z-index: 1000">
  <div hidden class="Toast Toast--loading">
    <span class="Toast-icon">
      <svg class="Toast--spinner" viewBox="0 0 32 32" width="18" height="18" aria-hidden="true">
        <path
          fill="#959da5"
          d="M16 0 A16 16 0 0 0 16 32 A16 16 0 0 0 16 0 M16 4 A12 12 0 0 1 16 28 A12 12 0 0 1 16 4"
        />
        <path fill="#ffffff" d="M16 0 A16 16 0 0 1 32 16 L28 16 A12 12 0 0 0 16 4z"></path>
      </svg>
    </span>
    <span class="Toast-content"></span>
  </div>

  <div hidden class="anim-fade-in fast Toast Toast--error">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-stop">
    <path d="M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.14.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>

  <div hidden class="anim-fade-in fast Toast Toast--warning">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>


  <div hidden class="anim-fade-in fast Toast Toast--success">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>

  <div hidden class="anim-fade-in fast Toast">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-info">
    <path d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8Zm8-6.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13ZM6.5 7.75A.75.75 0 0 1 7.25 7h1a.75.75 0 0 1 .75.75v2.75h.25a.75.75 0 0 1 0 1.5h-2a.75.75 0 0 1 0-1.5h.25v-2h-.25a.75.75 0 0 1-.75-.75ZM8 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>
</div>


  <div
    class="application-main "
    data-commit-hovercards-enabled
    data-discussion-hovercards-enabled
    data-issue-and-pr-hovercards-enabled
  >
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container" >
      
      
      
    

    






    
  <div id="repository-container-header" data-turbo-replace hidden></div>




<turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="">
    <div id="repo-content-pjax-container" class="repository-content " >
      <a href="https://github.dev/" class="d-none js-github-dev-shortcut" data-hotkey=".,Alt+Meta+≥,Control+Alt+.">Open in github.dev</a>
  <a href="https://github.dev/" class="d-none js-github-dev-new-tab-shortcut" data-hotkey="Shift+.,Shift+&gt;,&gt;" target="_blank" rel="noopener noreferrer">Open in a new github.dev tab</a>
    <a class="d-none" data-hotkey=",,Alt+Meta+≤,Control+Alt+," target="_blank" href="/codespaces/new/twisted/twisted/tree/trunk?resume=1">Open in codespace</a>



    
      
    





<react-app
  app-name="react-code-view"
  initial-path="/twisted/twisted/blob/trunk/README.rst"
  style="min-height: calc(100vh - 62px)"
  data-ssr="true"
  data-lazy="false"
  data-alternate="false"
>
  
  <script type="application/json" data-target="react-app.embeddedData">{"payload":{"allShortcutsEnabled":true,"fileTree":{"":{"items":[{"name":".github","path":".github","contentType":"directory"},{"name":"admin","path":"admin","contentType":"directory"},{"name":"bin","path":"bin","contentType":"directory"},{"name":"docs","path":"docs","contentType":"directory"},{"name":"src","path":"src","contentType":"directory"},{"name":".coveragerc","path":".coveragerc","contentType":"file"},{"name":".git-blame-ignore-revs","path":".git-blame-ignore-revs","contentType":"file"},{"name":".gitattributes","path":".gitattributes","contentType":"file"},{"name":".gitignore","path":".gitignore","contentType":"file"},{"name":".pre-commit-config.yaml","path":".pre-commit-config.yaml","contentType":"file"},{"name":".readthedocs.yml","path":".readthedocs.yml","contentType":"file"},{"name":"CONTRIBUTING.md","path":"CONTRIBUTING.md","contentType":"file"},{"name":"INSTALL.rst","path":"INSTALL.rst","contentType":"file"},{"name":"LICENSE","path":"LICENSE","contentType":"file"},{"name":"NEWS.rst","path":"NEWS.rst","contentType":"file"},{"name":"README.rst","path":"README.rst","contentType":"file"},{"name":"code_of_conduct.md","path":"code_of_conduct.md","contentType":"file"},{"name":"codecov.yml","path":"codecov.yml","contentType":"file"},{"name":"hatch_build.py","path":"hatch_build.py","contentType":"file"},{"name":"pyproject.toml","path":"pyproject.toml","contentType":"file"},{"name":"setup.cfg","path":"setup.cfg","contentType":"file"},{"name":"tox.ini","path":"tox.ini","contentType":"file"}],"totalCount":22}},"fileTreeProcessingTime":4.971093000000001,"foldersToFetch":[],"reducedMotionEnabled":"system","repo":{"id":1985358,"defaultBranch":"trunk","name":"twisted","ownerLogin":"twisted","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2011-07-01T22:40:42.000+02:00","ownerAvatar":"https://avatars.githubusercontent.com/u/716546?v=4","public":true,"private":false,"isOrgOwned":true},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"trunk","listCacheKey":"v0:1697146874.0","canEdit":true,"refType":"branch","currentOid":"157cd8e659705940e895d321339d467e76ae9d0a"},"path":"README.rst","currentUser":{"id":16610768,"login":"AleksNeStu","userEmail":"a.v.nesterovich@gmail.com"},"blob":{"rawLines":null,"stylingDirectives":null,"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/twisted/twisted/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":false,"repoAlertsPath":"/twisted/twisted/security/dependabot","repoSecurityAndAnalysisPath":"/twisted/twisted/settings/security_analysis","repoOwnerIsOrg":true,"currentUserCanAdminRepo":false},"displayName":"README.rst","displayUrl":"https://github.com/twisted/twisted/blob/trunk/README.rst?raw=true","headerInfo":{"blobSize":"4.42 KB","deleteInfo":{"deleteTooltip":"Fork this repository and delete the file"},"editInfo":{"editTooltip":"Fork this repository and edit the file"},"ghDesktopPath":"x-github-client://openRepo/https://github.com/twisted/twisted?branch=trunk\u0026filepath=README.rst","gitLfsPath":null,"onBranch":true,"shortPath":"73783ca","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Ftwisted%2Ftwisted%2Fblob%2Ftrunk%2FREADME.rst","isCSV":false,"isRichtext":true,"toc":[{"level":1,"text":"Twisted","anchor":"twisted","htmlText":"Twisted"},{"level":2,"text":"What is this?","anchor":"what-is-this","htmlText":"What is this?"},{"level":2,"text":"Installing","anchor":"installing","htmlText":"Installing"},{"level":2,"text":"Documentation and Support","anchor":"documentation-and-support","htmlText":"Documentation and Support"},{"level":2,"text":"Unit Tests","anchor":"unit-tests","htmlText":"Unit Tests"},{"level":2,"text":"Static Code Checkers","anchor":"static-code-checkers","htmlText":"Static Code Checkers"},{"level":2,"text":"Copyright","anchor":"copyright","htmlText":"Copyright"},{"level":2,"text":"Warranty","anchor":"warranty","htmlText":"Warranty"}],"lineInfo":{"truncatedLoc":"123","truncatedSloc":"77"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"reStructuredText","languageID":419,"large":false,"loggedIn":true,"newDiscussionPath":"/twisted/twisted/discussions/new","newIssuePath":"/twisted/twisted/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/twisted/twisted/blob/trunk/README.rst","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/twisted/twisted/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"rawBlobUrl":"https://github.com/twisted/twisted/raw/trunk/README.rst","renderImageOrRaw":false,"richText":"\u003carticle class=\"markdown-body entry-content container-lg\" itemprop=\"text\"\u003e\u003ch1 tabindex=\"-1\" id=\"user-content-twisted\" dir=\"auto\"\u003e\u003ca class=\"heading-link\" href=\"#twisted\"\u003eTwisted\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/h1\u003e\n\u003cp dir=\"auto\"\u003e\u003ca href=\"https://gitter.im/twisted/twisted\" rel=\"nofollow\"\u003e\u003cimg alt=\"gitter\" src=\"https://camo.githubusercontent.com/36f12e64939abe7eaaf00e9e2377940ea0b4405b12ca5dcc1431635dd2febee1/68747470733a2f2f696d672e736869656c64732e696f2f6769747465722f726f6f6d2f747769737465642f747769737465642e737667\" data-canonical-src=\"https://img.shields.io/gitter/room/twisted/twisted.svg\" style=\"max-width: 100%;\"\u003e\n\u003c/a\u003e\n\u003ca href=\"https://docs.twistedmatrix.com\" rel=\"nofollow\"\u003e\u003cimg alt=\"rtd\" src=\"https://camo.githubusercontent.com/0737bc1c19c49f509d4db9e23476bf3f9a0567f602672138b7aeff8002a53bdb/68747470733a2f2f72656164746865646f63732e6f72672f70726f6a656374732f747769737465642f62616467652f3f76657273696f6e3d6c6174657374267374796c653d666c6174\" data-canonical-src=\"https://readthedocs.org/projects/twisted/badge/?version=latest\u0026amp;style=flat\" style=\"max-width: 100%;\"\u003e\u003c/a\u003e\n\u003ca href=\"https://pypi.python.org/pypi/twisted\" rel=\"nofollow\"\u003e\u003cimg alt=\"pypi\" src=\"https://camo.githubusercontent.com/ab2e87784e4c40ac138408a6d5d6c39351694fc517b4da12649cb4acd882bcde/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f747769737465642e737667\" data-canonical-src=\"https://img.shields.io/pypi/v/twisted.svg\" style=\"max-width: 100%;\"\u003e\n\u003c/a\u003e\n\u003ca href=\"https://github.com/twisted/twisted\"\u003e\u003cimg alt=\"ci\" src=\"https://github.com/twisted/twisted/actions/workflows/test.yaml/badge.svg\" style=\"max-width: 100%;\"\u003e\n\u003c/a\u003e\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eFor information on changes in this release, see the \u003ca href=\"/twisted/twisted/blob/trunk/NEWS.rst\"\u003eNEWS\u003c/a\u003e file.\u003c/p\u003e\n\u003ca name=\"user-content-what-is-this\"\u003e\u003c/a\u003e\n\u003ch2 tabindex=\"-1\" id=\"user-content-what-is-this\" dir=\"auto\"\u003e\u003ca class=\"heading-link\" href=\"#what-is-this\"\u003eWhat is this?\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/h2\u003e\n\u003cp dir=\"auto\"\u003eTwisted is an event-based framework for internet applications, supporting Python 3.6+.\nIt includes modules for many different purposes, including the following:\u003c/p\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003e\u003ccode\u003etwisted.web\u003c/code\u003e: HTTP clients and servers, HTML templating, and a WSGI server\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003etwisted.conch\u003c/code\u003e: SSHv2 and Telnet clients and servers and terminal emulators\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003etwisted.words\u003c/code\u003e: Clients and servers for IRC, XMPP, and other IM protocols\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003etwisted.mail\u003c/code\u003e: IMAPv4, POP3, SMTP clients and servers\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003etwisted.positioning\u003c/code\u003e: Tools for communicating with NMEA-compatible GPS receivers\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003etwisted.names\u003c/code\u003e: DNS client and tools for making your own DNS servers\u003c/li\u003e\n\u003cli\u003e\u003ccode\u003etwisted.trial\u003c/code\u003e: A unit testing framework that integrates well with Twisted-based code.\u003c/li\u003e\n\u003c/ul\u003e\n\u003cp dir=\"auto\"\u003eTwisted supports all major system event loops -- \u003ccode\u003eselect\u003c/code\u003e (all platforms), \u003ccode\u003epoll\u003c/code\u003e (most POSIX platforms), \u003ccode\u003eepoll\u003c/code\u003e (Linux), \u003ccode\u003ekqueue\u003c/code\u003e (FreeBSD, macOS), IOCP (Windows), and various GUI event loops (GTK+2/3, Qt, wxWidgets).\nThird-party reactors can plug into Twisted, and provide support for additional event loops.\u003c/p\u003e\n\u003ca name=\"user-content-installing\"\u003e\u003c/a\u003e\n\u003ch2 tabindex=\"-1\" id=\"user-content-installing\" dir=\"auto\"\u003e\u003ca class=\"heading-link\" href=\"#installing\"\u003eInstalling\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/h2\u003e\n\u003cp dir=\"auto\"\u003eTo install the latest version of Twisted using pip:\u003c/p\u003e\n\u003cpre\u003e$ pip install twisted\n\u003c/pre\u003e\n\u003cp dir=\"auto\"\u003eAdditional instructions for installing this software are in \u003ca href=\"/twisted/twisted/blob/trunk/INSTALL.rst\"\u003ethe installation instructions\u003c/a\u003e.\u003c/p\u003e\n\u003ca name=\"user-content-documentation-and-support\"\u003e\u003c/a\u003e\n\u003ch2 tabindex=\"-1\" id=\"user-content-documentation-and-support\" dir=\"auto\"\u003e\u003ca class=\"heading-link\" href=\"#documentation-and-support\"\u003eDocumentation and Support\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/h2\u003e\n\u003cp dir=\"auto\"\u003eTwisted's documentation is available from the \u003ca href=\"https://twistedmatrix.com/documents/current/\" rel=\"nofollow\"\u003eTwisted Matrix website\u003c/a\u003e.\nThis documentation contains how-tos, code examples, and an API reference.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eHelp is also available on the \u003ca href=\"https://mail.python.org/mailman3/lists/twisted.python.org/\" rel=\"nofollow\"\u003eTwisted mailing list\u003c/a\u003e.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eThere is also an IRC channel, \u003ccode\u003e#twisted\u003c/code\u003e,\non the \u003ca href=\"https://libera.chat/\" rel=\"nofollow\"\u003eLibera.Chat\u003c/a\u003e network.\nA web client is available at \u003ca href=\"https://web.libera.chat/\" rel=\"nofollow\"\u003eweb.libera.chat\u003c/a\u003e.\u003c/p\u003e\n\u003ca name=\"user-content-unit-tests\"\u003e\u003c/a\u003e\n\u003ch2 tabindex=\"-1\" id=\"user-content-unit-tests\" dir=\"auto\"\u003e\u003ca class=\"heading-link\" href=\"#unit-tests\"\u003eUnit Tests\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/h2\u003e\n\u003cp dir=\"auto\"\u003eTwisted has a comprehensive test suite, which can be run by \u003ccode\u003etox\u003c/code\u003e:\u003c/p\u003e\n\u003cpre\u003e$ tox -l                       # to view all test environments\n$ tox -e nocov                 # to run all the tests without coverage\n$ tox -e withcov               # to run all the tests with coverage\n$ tox -e alldeps-withcov-posix # install all dependencies, run tests with coverage on POSIX platform\n\u003c/pre\u003e\n\u003cp dir=\"auto\"\u003eYou can test running the test suite under the different reactors with the \u003ccode\u003eTWISTED_REACTOR\u003c/code\u003e environment variable:\u003c/p\u003e\n\u003cpre\u003e$ env TWISTED_REACTOR=epoll tox -e alldeps-withcov-posix\n\u003c/pre\u003e\n\u003cp dir=\"auto\"\u003eSome of these tests may fail if you:\u003c/p\u003e\n\u003cul dir=\"auto\"\u003e\n\u003cli\u003edon't have the dependencies required for a particular subsystem installed,\u003c/li\u003e\n\u003cli\u003ehave a firewall blocking some ports (or things like Multicast, which Linux NAT has shown itself to do), or\u003c/li\u003e\n\u003cli\u003erun them as root.\u003c/li\u003e\n\u003c/ul\u003e\n\u003ca name=\"user-content-static-code-checkers\"\u003e\u003c/a\u003e\n\u003ch2 tabindex=\"-1\" id=\"user-content-static-code-checkers\" dir=\"auto\"\u003e\u003ca class=\"heading-link\" href=\"#static-code-checkers\"\u003eStatic Code Checkers\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/h2\u003e\n\u003cp dir=\"auto\"\u003eYou can ensure that code complies to Twisted \u003ca href=\"https://twistedmatrix.com/documents/current/core/development/policy/coding-standard.html\" rel=\"nofollow\"\u003ecoding standards\u003c/a\u003e:\u003c/p\u003e\n\u003cpre\u003e$ tox -e lint   # run pre-commit to check coding stanards\n$ tox -e mypy   # run MyPy static type checker to check for type errors\n\u003c/pre\u003e\n\u003cp dir=\"auto\"\u003eOr, for speed, use pre-commit directly:\u003c/p\u003e\n\u003cpre\u003e$ pipx run pre-commit run\n\u003c/pre\u003e\n\u003ca name=\"user-content-copyright\"\u003e\u003c/a\u003e\n\u003ch2 tabindex=\"-1\" id=\"user-content-copyright\" dir=\"auto\"\u003e\u003ca class=\"heading-link\" href=\"#copyright\"\u003eCopyright\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/h2\u003e\n\u003cp dir=\"auto\"\u003eAll of the code in this distribution is Copyright (c) 2001-2023 Twisted Matrix Laboratories.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eTwisted is made available under the MIT license.\nThe included \u003ca href=\"/twisted/twisted/blob/trunk/LICENSE\"\u003eLICENSE\u003c/a\u003e file describes this in detail.\u003c/p\u003e\n\u003ca name=\"user-content-warranty\"\u003e\u003c/a\u003e\n\u003ch2 tabindex=\"-1\" id=\"user-content-warranty\" dir=\"auto\"\u003e\u003ca class=\"heading-link\" href=\"#warranty\"\u003eWarranty\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/h2\u003e\n\u003cblockquote\u003e\n\u003cp dir=\"auto\"\u003eTHIS SOFTWARE IS PROVIDED \"AS IS\" WITHOUT WARRANTY OF ANY KIND, EITHER\nEXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES\nOF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS\nTO THE USE OF THIS SOFTWARE IS WITH YOU.\u003c/p\u003e\n\u003cp dir=\"auto\"\u003eIN NO EVENT WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY\nAND/OR REDISTRIBUTE THE LIBRARY, BE LIABLE TO YOU FOR ANY DAMAGES, EVEN IF\nSUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH\nDAMAGES.\u003c/p\u003e\n\u003c/blockquote\u003e\n\u003cp dir=\"auto\"\u003eAgain, see the included \u003ca href=\"/twisted/twisted/blob/trunk/LICENSE\"\u003eLICENSE\u003c/a\u003e file for specific legal details.\u003c/p\u003e\n\n\u003c/article\u003e","renderedFileInfo":null,"shortPath":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"twisted","repoName":"twisted","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timedOut":false,"notAnalyzed":true,"symbols":[]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/twisted/twisted/branches":{"post":"DWNDsY_7qgTTzOezB69GBmfMTm_8pW5KmQxYBTVIJoR0Wo3Rl4fF7mcO7J8oZsJjds57tYaldgU09bBgtivJRw"},"/repos/preferences":{"post":"4OMxzAM9xhWxi8ELDlZZWt2q7NLxCg6SOHpw2k_EpL1dhLVawx5SIyjfDW7JNKvHVfNbzbnxnqtEYlckSIqrXg"}}},"title":"twisted/README.rst at trunk · twisted/twisted","appPayload":{"helpUrl":"https://docs.github.com","findFileWorkerPath":"/assets-cdn/worker/find-file-worker-3722b59160bc.js","findInFileWorkerPath":"/assets-cdn/worker/find-in-file-worker-b812db9596b1.js","githubDevUrl":"https://github.dev/","enabled_features":{"code_nav_ui_events":false,"copilot_conversational_ux":false,"copilot_conversational_ux_embedding_update":false,"copilot_conversational_ux_streaming":true,"copilot_popover_file_editor_header":true,"copilot_smell_icebreaker_ux":false}}}</script>
  <div data-target="react-app.reactRoot"><style data-styled="true" data-styled-version="5.3.6">.fNPcqd{font-weight:600;font-size:32px;margin:0;font-size:14px;}/*!sc*/
.imcwCi{font-weight:600;font-size:32px;margin:0;font-size:16px;margin-left:8px;}/*!sc*/
.cgQnMS{font-weight:600;font-size:32px;margin:0;}/*!sc*/
.diwsLq{font-weight:600;font-size:32px;margin:0;font-weight:600;display:inline-block;max-width:100%;font-size:16px;}/*!sc*/
.jAEDJk{font-weight:600;font-size:32px;margin:0;font-weight:600;display:inline-block;max-width:100%;font-size:14px;}/*!sc*/
data-styled.g1[id="Heading__StyledHeading-sc-1c1dgg0-0"]{content:"fNPcqd,imcwCi,cgQnMS,diwsLq,jAEDJk,"}/*!sc*/
.fSWWem{padding:0;}/*!sc*/
.kPPmzM{max-width:100%;margin-left:auto;margin-right:auto;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;}/*!sc*/
.cIAPDV{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex:1 1 100%;-ms-flex:1 1 100%;flex:1 1 100%;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;max-width:100%;}/*!sc*/
.gvCnwW{width:100%;}/*!sc*/
@media screen and (min-width:544px){.gvCnwW{width:100%;}}/*!sc*/
@media screen and (min-width:768px){.gvCnwW{width:auto;}}/*!sc*/
.ioxSsX{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-order:1;-ms-flex-order:1;order:1;width:100%;margin-left:0;margin-right:0;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;margin-bottom:0;min-width:0;}/*!sc*/
@media screen and (min-width:544px){.ioxSsX{-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;}}/*!sc*/
@media screen and (min-width:768px){.ioxSsX{width:auto;margin-top:0 !important;margin-bottom:0 !important;position:-webkit-sticky;position:sticky;top:0px;max-height:var(--sticky-pane-height);-webkit-flex-direction:row-reverse;-ms-flex-direction:row-reverse;flex-direction:row-reverse;margin-right:0;}}/*!sc*/
@media screen and (min-width:769px){.ioxSsX{height:100vh;max-height:100vh !important;}}/*!sc*/
@media print,screen and (max-width:1011px) and (min-width:768px){.ioxSsX{display:none;}}/*!sc*/
.eUyHuk{margin-left:0;margin-right:0;display:none;margin-top:0;}/*!sc*/
@media screen and (min-width:768px){.eUyHuk{margin-left:0 !important;margin-right:0 !important;}}/*!sc*/
.hAeDYA{height:100%;position:relative;display:none;margin-left:0;}/*!sc*/
.hYdBkT{position:absolute;inset:0 -2px;cursor:col-resize;background-color:transparent;-webkit-transition-delay:0.1s;transition-delay:0.1s;}/*!sc*/
.hYdBkT:hover{background-color:rgba(99,110,123,0.4);}/*!sc*/
.gNdDUH{--pane-min-width:256px;--pane-max-width-diff:511px;--pane-max-width:calc(100vw - var(--pane-max-width-diff));width:100%;padding:0;}/*!sc*/
@media screen and (min-width:544px){}/*!sc*/
@media screen and (min-width:768px){.gNdDUH{width:clamp(var(--pane-min-width),var(--pane-width),var(--pane-max-width));overflow:auto;}}/*!sc*/
@media screen and (min-width:1280px){.gNdDUH{--pane-max-width-diff:959px;}}/*!sc*/
.jywUSN{max-height:100%;height:100%;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;}/*!sc*/
@media screen and (max-width:768px){.jywUSN{display:none;}}/*!sc*/
@media screen and (min-width:768px){.jywUSN{max-height:100vh;height:100vh;}}/*!sc*/
.hBSSUC{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;padding-left:16px;padding-right:16px;padding-bottom:8px;padding-top:16px;}/*!sc*/
.iPurHz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;width:100%;margin-bottom:16px;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;}/*!sc*/
.kkrdEu{-webkit-box-pack:center;-webkit-justify-content:center;-ms-flex-pack:center;justify-content:center;}/*!sc*/
.trpoQ{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;pointer-events:none;}/*!sc*/
.hVHHYa{margin-left:24px;margin-right:24px;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;width:100%;}/*!sc*/
.idZfsJ{-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;}/*!sc*/
.bKgizp{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;width:100%;}/*!sc*/
.fxhqJs{margin-right:4px;color:#768390;}/*!sc*/
.caeYDk{font-size:14px;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}/*!sc*/
.jahcnb{margin-left:8px;white-space:nowrap;}/*!sc*/
.jahcnb:hover button:not(:hover){border-left-color:var(--button-default-borderColor-hover,var(--color-btn-hover-border));}/*!sc*/
.ccToMy{margin-left:16px;margin-right:16px;margin-bottom:12px;}/*!sc*/
@media screen and (max-width:768px){.ccToMy{display:none;}}/*!sc*/
.cNvKlH{margin-right:-6px;}/*!sc*/
.cLfAnm{-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;max-height:100% !important;overflow-y:auto;-webkit-scrollbar-gutter:stable;-moz-scrollbar-gutter:stable;-ms-scrollbar-gutter:stable;scrollbar-gutter:stable;}/*!sc*/
@media screen and (max-width:768px){.cLfAnm{display:none;}}/*!sc*/
.erWCJP{padding-left:16px;padding-right:16px;padding-bottom:8px;}/*!sc*/
@media (min-height:600px) and (min-width:768px){.hwhShM{display:none;}}/*!sc*/
.cYPxpP{margin-top:8px;margin-left:16px;margin-right:16px;margin-bottom:12px;font-size:12px;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;}/*!sc*/
@media (max-height:599px),(max-width:767px){.fBtiVT{display:none;}}/*!sc*/
.emFMJu{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-order:2;-ms-flex-order:2;order:2;-webkit-flex-basis:0;-ms-flex-preferred-size:0;flex-basis:0;-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;-webkit-flex-shrink:1;-ms-flex-negative:1;flex-shrink:1;min-width:1px;margin-right:auto;}/*!sc*/
@media print{.emFMJu{display:-webkit-box !important;display:-webkit-flex !important;display:-ms-flexbox !important;display:flex !important;}}/*!sc*/
.hlUAHL{width:100%;max-width:100%;margin-left:auto;margin-right:auto;-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;padding:0;}/*!sc*/
.iStsmI{margin-left:auto;margin-right:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;padding-bottom:40px;max-width:100%;margin-top:0;}/*!sc*/
.eIgvIk{display:inherit;}/*!sc*/
.eVFfWF{width:100%;}/*!sc*/
.kgXdnT{padding:16px;padding-bottom:0;}/*!sc*/
.kzTa-dF{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;gap:16px;width:100%;}/*!sc*/
.bbXCl{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:start;-webkit-box-align:start;-ms-flex-align:start;align-items:start;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;}/*!sc*/
.hGGMNu{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:start;-webkit-box-align:start;-ms-flex-align:start;align-items:start;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;justify-self:flex-end;}/*!sc*/
.eHRrYV{margin-left:8px;margin-right:8px;}/*!sc*/
.dKmYfk{font-size:14px;min-width:0;max-width:125px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}/*!sc*/
.hSNzKh{justify-self:end;max-width:100%;}/*!sc*/
.eTvGbF{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;font-size:16px;min-width:0;-webkit-flex-shrink:1;-ms-flex-negative:1;flex-shrink:1;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;max-width:100%;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;}/*!sc*/
.kzRgrI{max-width:100%;}/*!sc*/
.cmAPIB{max-width:100%;list-style:none;display:inline-block;}/*!sc*/
.jwXCBK{display:inline-block;max-width:100%;}/*!sc*/
.bDwCYs{padding:16px;padding-bottom:0;padding-left:16px;padding-right:16px;}/*!sc*/
.fywjmm{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;gap:8px;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;width:100%;}/*!sc*/
.dyczTK{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:start;-webkit-box-align:start;-ms-flex-align:start;align-items:start;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;gap:8px;}/*!sc*/
.kszRgZ{-webkit-align-self:center;-ms-flex-item-align:center;align-self:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;padding-right:8px;min-width:0;}/*!sc*/
.gtBUEp{min-height:32px;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:start;-webkit-box-align:start;-ms-flex-align:start;align-items:start;}/*!sc*/
.MERGN{margin-left:16px;margin-right:16px;}/*!sc*/
@media screen and (min-width:1440px){.MERGN{margin-left:16px;}}/*!sc*/
.cMYnca{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;}/*!sc*/
.dfEVSV{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;border:1px solid;border-color:#444c56;border-radius:6px;margin-bottom:16px;}/*!sc*/
.eYedVD{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;gap:8px;min-width:273px;padding-right:8px;padding-left:16px;padding-top:8px;padding-bottom:8px;}/*!sc*/
.jGfYmh{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;gap:8px;}/*!sc*/
.lhFvfi{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;}/*!sc*/
.bqgLjk{display:inherit;}/*!sc*/
@media screen and (min-width:544px){.bqgLjk{display:none;}}/*!sc*/
@media screen and (min-width:768px){.bqgLjk{display:none;}}/*!sc*/
.iJmJly{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;}/*!sc*/
.jACbi{width:100%;height:-webkit-fit-content;height:-moz-fit-content;height:fit-content;min-width:0;margin-right:0;}/*!sc*/
.bSdwWB{padding-left:4px;padding-bottom:16px;}/*!sc*/
.fleZSW{-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;}/*!sc*/
.jALzIY{font-size:12px;-webkit-flex:auto;-ms-flex:auto;flex:auto;padding-right:16px;color:#768390;min-width:0;}/*!sc*/
.gBKNLX{top:0px;z-index:1;background:var(--color-canvas-default);position:-webkit-sticky;position:sticky;}/*!sc*/
.ePiodO{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;width:100%;position:absolute;}/*!sc*/
.kQJlnf{display:none;min-width:0;padding-top:8px;padding-bottom:8px;}/*!sc*/
.gJICKO{margin-right:8px;margin-left:16px;text-overflow:ellipsis;overflow:hidden;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;width:100%;}/*!sc*/
.iZJewz{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:row;-ms-flex-direction:row;flex-direction:row;font-size:14px;min-width:0;-webkit-flex-shrink:1;-ms-flex-negative:1;flex-shrink:1;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;max-width:100%;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;}/*!sc*/
.jgMUtU{padding-left:8px;padding-top:8px;padding-bottom:8px;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex:1;-ms-flex:1;flex:1;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;background-color:#2d333b;border:1px solid var(--borderColor-default,var(--color-border-default));border-radius:6px 6px 0px 0px;}/*!sc*/
.bfkNRF{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;gap:8px;min-width:0;}/*!sc*/
.fXBLEV{display:block;position:relative;-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;margin-top:-1px;margin-bottom:-1px;--separator-color:transparent;}/*!sc*/
.fXBLEV:not(:last-child){margin-right:1px;}/*!sc*/
.fXBLEV:not(:last-child):after{background-color:var(--separator-color);content:"";position:absolute;right:-2px;top:8px;bottom:8px;width:1px;}/*!sc*/
.fXBLEV:focus-within:has(:focus-visible){--separator-color:transparent;}/*!sc*/
.fXBLEV:first-child{margin-left:-1px;}/*!sc*/
.fXBLEV:last-child{margin-right:-1px;}/*!sc*/
.eejbCg{display:block;position:relative;-webkit-box-flex:1;-webkit-flex-grow:1;-ms-flex-positive:1;flex-grow:1;margin-top:-1px;margin-bottom:-1px;--separator-color:#444c56;}/*!sc*/
.eejbCg:not(:last-child){margin-right:1px;}/*!sc*/
.eejbCg:not(:last-child):after{background-color:var(--separator-color);content:"";position:absolute;right:-2px;top:8px;bottom:8px;width:1px;}/*!sc*/
.eejbCg:focus-within:has(:focus-visible){--separator-color:transparent;}/*!sc*/
.eejbCg:first-child{margin-left:-1px;}/*!sc*/
.eejbCg:last-child{margin-right:-1px;}/*!sc*/
.iBylDf{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;gap:8px;margin-right:8px;}/*!sc*/
.kSGBPx{gap:8px;}/*!sc*/
.dWbgpS{border:1px solid;border-top:none;border-color:#444c56;border-radius:0px 0px 6px 6px;min-width:273px;}/*!sc*/
.eRvpKx{background-color:var(--bgColor-default,var(--color-canvas-default));border:0px;border-width:0;border-radius:0px 0px 6px 6px;padding:0;min-width:0;margin-top:46px;-webkit-box-pack:center;-webkit-justify-content:center;-ms-flex-pack:center;justify-content:center;}/*!sc*/
.cTsUqU{border-bottom-left-radius:6px;border-bottom-right-radius:6px;padding:32px;min-width:0;}/*!sc*/
.aZrVR{position:fixed;top:0;right:0;height:100%;width:15px;-webkit-transition:-webkit-transform 0.3s;-webkit-transition:transform 0.3s;transition:transform 0.3s;z-index:1;}/*!sc*/
.aZrVR:hover{-webkit-transform:scaleX(1.5);-ms-transform:scaleX(1.5);transform:scaleX(1.5);}/*!sc*/
data-styled.g2[id="Box-sc-g0xbh4-0"]{content:"fSWWem,kPPmzM,cIAPDV,gvCnwW,ioxSsX,eUyHuk,hAeDYA,hYdBkT,gNdDUH,jywUSN,hBSSUC,iPurHz,kkrdEu,trpoQ,hVHHYa,idZfsJ,bKgizp,fxhqJs,caeYDk,jahcnb,ccToMy,cNvKlH,cLfAnm,erWCJP,hwhShM,cYPxpP,fBtiVT,emFMJu,hlUAHL,iStsmI,eIgvIk,eVFfWF,kgXdnT,kzTa-dF,bbXCl,hGGMNu,eHRrYV,dKmYfk,hSNzKh,eTvGbF,kzRgrI,cmAPIB,jwXCBK,bDwCYs,fywjmm,dyczTK,kszRgZ,gtBUEp,MERGN,cMYnca,dfEVSV,eYedVD,jGfYmh,lhFvfi,bqgLjk,iJmJly,jACbi,bSdwWB,fleZSW,jALzIY,gBKNLX,ePiodO,kQJlnf,gJICKO,iZJewz,jgMUtU,bfkNRF,fXBLEV,eejbCg,iBylDf,kSGBPx,dWbgpS,eRvpKx,cTsUqU,aZrVR,"}/*!sc*/
.rTZSs{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;-webkit-clip:rect(0,0,0,0);clip:rect(0,0,0,0);white-space:nowrap;border-width:0;}/*!sc*/
data-styled.g4[id="_VisuallyHidden__VisuallyHidden-sc-11jhm7a-0"]{content:"rTZSs,"}/*!sc*/
.fUpWeN{display:inline-block;overflow:hidden;text-overflow:ellipsis;vertical-align:top;white-space:nowrap;max-width:125px;max-width:100%;}/*!sc*/
data-styled.g6[id="Truncate__StyledTruncate-sc-23o1d2-0"]{content:"fUpWeN,"}/*!sc*/
.gPmdpC{color:#539bf5;-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.gPmdpC:hover{-webkit-text-decoration:underline;text-decoration:underline;}/*!sc*/
.gPmdpC:is(button){display:inline-block;padding:0;font-size:inherit;white-space:nowrap;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;background-color:transparent;border:0;-webkit-appearance:none;-moz-appearance:none;appearance:none;}/*!sc*/
.bQnDDD{color:#539bf5;-webkit-text-decoration:none;text-decoration:none;font-weight:600;}/*!sc*/
.bQnDDD:hover{-webkit-text-decoration:underline;text-decoration:underline;}/*!sc*/
.bQnDDD:is(button){display:inline-block;padding:0;font-size:inherit;white-space:nowrap;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;background-color:transparent;border:0;-webkit-appearance:none;-moz-appearance:none;appearance:none;}/*!sc*/
data-styled.g8[id="Link__StyledLink-sc-14289xe-0"]{content:"gPmdpC,bQnDDD,"}/*!sc*/
.iOFiIT{font-size:14px;line-height:20px;color:#adbac7;vertical-align:middle;background-color:#22272e;border:1px solid var(--control-borderColor-rest,#444c56);border-radius:6px;outline:none;box-shadow:0 0 transparent;display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;-webkit-align-items:stretch;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;min-height:32px;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;min-width:200px;}/*!sc*/
.iOFiIT input,.iOFiIT textarea{cursor:text;}/*!sc*/
.iOFiIT select{cursor:pointer;}/*!sc*/
.iOFiIT::-webkit-input-placeholder{color:#636e7b;}/*!sc*/
.iOFiIT::-moz-placeholder{color:#636e7b;}/*!sc*/
.iOFiIT:-ms-input-placeholder{color:#636e7b;}/*!sc*/
.iOFiIT::placeholder{color:#636e7b;}/*!sc*/
.iOFiIT:focus-within{border-color:#539bf5;outline:none;box-shadow:inset 0 0 0 1px #539bf5;}/*!sc*/
.iOFiIT > textarea{padding:12px;}/*!sc*/
@media (min-width:768px){.iOFiIT{font-size:14px;}}/*!sc*/
data-styled.g26[id="TextInputWrapper__TextInputBaseWrapper-sc-1mqhpbi-0"]{content:"iOFiIT,"}/*!sc*/
.fvMdhy{background-repeat:no-repeat;background-position:right 8px center;padding-left:12px;padding-right:12px;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;min-width:200px;}/*!sc*/
.fvMdhy > :not(:last-child){margin-right:8px;}/*!sc*/
.fvMdhy .TextInput-icon,.fvMdhy .TextInput-action{-webkit-align-self:center;-ms-flex-item-align:center;align-self:center;color:#768390;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;}/*!sc*/
.fvMdhy > input,.fvMdhy > select{padding-left:0;padding-right:0;}/*!sc*/
data-styled.g27[id="TextInputWrapper-sc-1mqhpbi-1"]{content:"fvMdhy,"}/*!sc*/
.bWtVmw{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#539bf5;background-color:transparent;box-shadow:none;}/*!sc*/
.bWtVmw:focus:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.bWtVmw:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.bWtVmw:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.bWtVmw[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.bWtVmw[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.bWtVmw:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.bWtVmw:active{-webkit-transition:none;transition:none;}/*!sc*/
.bWtVmw:disabled{cursor:not-allowed;box-shadow:none;color:#545d68;}/*!sc*/
.bWtVmw:disabled [data-component=ButtonCounter],.bWtVmw:disabled [data-component="leadingVisual"],.bWtVmw:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.bWtVmw:focus{outline:solid 1px transparent;}}/*!sc*/
.bWtVmw [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.bWtVmw[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.bWtVmw[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.bWtVmw[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.bWtVmw[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.bWtVmw[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.bWtVmw[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.bWtVmw[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.bWtVmw[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.bWtVmw[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.bWtVmw[data-block="block"]{width:100%;}/*!sc*/
.bWtVmw [data-component="leadingVisual"]{grid-area:leadingVisual;color:#768390;}/*!sc*/
.bWtVmw [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.bWtVmw [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.bWtVmw [data-component="trailingAction"]{margin-right:-4px;color:#768390;}/*!sc*/
.bWtVmw [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.bWtVmw [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.bWtVmw:hover:not([disabled]){background-color:#444c56;}/*!sc*/
.bWtVmw:active:not([disabled]){background-color:#2d333b;}/*!sc*/
.bWtVmw[aria-expanded=true]{background-color:#2d333b;}/*!sc*/
.bWtVmw[data-component="IconButton"][data-no-visuals]{color:#768390;}/*!sc*/
.bWtVmw[data-no-visuals]{color:#539bf5;}/*!sc*/
.bWtVmw:has([data-component="ButtonCounter"]){color:#539bf5;}/*!sc*/
.bWtVmw:disabled[data-no-visuals]{color:#545d68;}/*!sc*/
.bWtVmw:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.bWtVmw{color:#768390;padding-left:8px;padding-right:8px;display:none;}/*!sc*/
@media screen and (max-width:768px){.bWtVmw{display:block;}}/*!sc*/
.imyHbr{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#539bf5;background-color:transparent;box-shadow:none;}/*!sc*/
.imyHbr:focus:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.imyHbr:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.imyHbr:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.imyHbr[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.imyHbr[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.imyHbr:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.imyHbr:active{-webkit-transition:none;transition:none;}/*!sc*/
.imyHbr:disabled{cursor:not-allowed;box-shadow:none;color:#545d68;}/*!sc*/
.imyHbr:disabled [data-component=ButtonCounter],.imyHbr:disabled [data-component="leadingVisual"],.imyHbr:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.imyHbr:focus{outline:solid 1px transparent;}}/*!sc*/
.imyHbr [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.imyHbr[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.imyHbr[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.imyHbr[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.imyHbr[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.imyHbr[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.imyHbr[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.imyHbr[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.imyHbr[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.imyHbr[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.imyHbr[data-block="block"]{width:100%;}/*!sc*/
.imyHbr [data-component="leadingVisual"]{grid-area:leadingVisual;color:#768390;}/*!sc*/
.imyHbr [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.imyHbr [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.imyHbr [data-component="trailingAction"]{margin-right:-4px;color:#768390;}/*!sc*/
.imyHbr [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.imyHbr [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.imyHbr:hover:not([disabled]){background-color:#444c56;}/*!sc*/
.imyHbr:active:not([disabled]){background-color:#2d333b;}/*!sc*/
.imyHbr[aria-expanded=true]{background-color:#2d333b;}/*!sc*/
.imyHbr[data-component="IconButton"][data-no-visuals]{color:#768390;}/*!sc*/
.imyHbr[data-no-visuals]{color:#768390;height:32px;position:relative;}/*!sc*/
@media screen and (max-width:768px){.imyHbr[data-no-visuals]{display:none;}}/*!sc*/
.imyHbr:has([data-component="ButtonCounter"]){color:#539bf5;}/*!sc*/
.imyHbr:disabled[data-no-visuals]{color:#545d68;}/*!sc*/
.imyHbr:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.eJRzxr{border-radius:6px;border:1px solid;border-color:rgba(205,217,229,0.1);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#adbac7;background-color:#373e47;box-shadow:0 0 transparent,0 0 transparent;}/*!sc*/
.eJRzxr:focus:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.eJRzxr:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.eJRzxr:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.eJRzxr[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.eJRzxr[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.eJRzxr:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.eJRzxr:active{-webkit-transition:none;transition:none;}/*!sc*/
.eJRzxr:disabled{cursor:not-allowed;box-shadow:none;color:#545d68;}/*!sc*/
.eJRzxr:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.eJRzxr:focus{outline:solid 1px transparent;}}/*!sc*/
.eJRzxr [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.eJRzxr[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.eJRzxr[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.eJRzxr[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.eJRzxr[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.eJRzxr[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.eJRzxr[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.eJRzxr[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.eJRzxr[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.eJRzxr[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.eJRzxr[data-block="block"]{width:100%;}/*!sc*/
.eJRzxr [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.eJRzxr [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.eJRzxr [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.eJRzxr [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.eJRzxr [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.eJRzxr [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.eJRzxr:hover:not([disabled]){background-color:#444c56;border-color:#768390;}/*!sc*/
.eJRzxr:active:not([disabled]){background-color:hsla(213,12%,27%,1);border-color:#636e7b;}/*!sc*/
.eJRzxr[aria-expanded=true]{background-color:hsla(213,12%,27%,1);border-color:#636e7b;}/*!sc*/
.eJRzxr [data-component="leadingVisual"],.eJRzxr [data-component="trailingVisual"],.eJRzxr [data-component="trailingAction"]{color:var(--button-color,#768390);}/*!sc*/
.eJRzxr{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;min-width:0;}/*!sc*/
.eJRzxr svg{color:#768390;}/*!sc*/
.eJRzxr > span{width:inherit;}/*!sc*/
.eCoUah{border-radius:6px;border:1px solid;border-color:rgba(205,217,229,0.1);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#adbac7;background-color:#373e47;box-shadow:0 0 transparent,0 0 transparent;}/*!sc*/
.eCoUah:focus:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.eCoUah:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.eCoUah:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.eCoUah[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.eCoUah[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.eCoUah:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.eCoUah:active{-webkit-transition:none;transition:none;}/*!sc*/
.eCoUah:disabled{cursor:not-allowed;box-shadow:none;color:#545d68;}/*!sc*/
.eCoUah:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.eCoUah:focus{outline:solid 1px transparent;}}/*!sc*/
.eCoUah [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.eCoUah[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.eCoUah[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.eCoUah[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.eCoUah[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.eCoUah[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.eCoUah[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.eCoUah[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.eCoUah[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.eCoUah[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.eCoUah[data-block="block"]{width:100%;}/*!sc*/
.eCoUah [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.eCoUah [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.eCoUah [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.eCoUah [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.eCoUah [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.eCoUah [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.eCoUah:hover:not([disabled]){background-color:#444c56;border-color:#768390;}/*!sc*/
.eCoUah:active:not([disabled]){background-color:hsla(213,12%,27%,1);border-color:#636e7b;}/*!sc*/
.eCoUah[aria-expanded=true]{background-color:hsla(213,12%,27%,1);border-color:#636e7b;}/*!sc*/
.eCoUah [data-component="leadingVisual"],.eCoUah [data-component="trailingVisual"],.eCoUah [data-component="trailingAction"]{color:var(--button-color,#768390);}/*!sc*/
.eCoUah[data-no-visuals]{color:#636e7b;border-top-right-radius:0;border-bottom-right-radius:0;border-right:0;}/*!sc*/
.cIsLoD{border-radius:6px;border:1px solid;border-color:rgba(205,217,229,0.1);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#adbac7;background-color:#373e47;box-shadow:0 0 transparent,0 0 transparent;}/*!sc*/
.cIsLoD:focus:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.cIsLoD:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.cIsLoD:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.cIsLoD[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.cIsLoD[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.cIsLoD:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.cIsLoD:active{-webkit-transition:none;transition:none;}/*!sc*/
.cIsLoD:disabled{cursor:not-allowed;box-shadow:none;color:#545d68;}/*!sc*/
.cIsLoD:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.cIsLoD:focus{outline:solid 1px transparent;}}/*!sc*/
.cIsLoD [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.cIsLoD[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.cIsLoD[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.cIsLoD[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.cIsLoD[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.cIsLoD[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.cIsLoD[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.cIsLoD[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.cIsLoD[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.cIsLoD[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.cIsLoD[data-block="block"]{width:100%;}/*!sc*/
.cIsLoD [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.cIsLoD [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.cIsLoD [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.cIsLoD [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.cIsLoD [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.cIsLoD [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.cIsLoD:hover:not([disabled]){background-color:#444c56;border-color:#768390;}/*!sc*/
.cIsLoD:active:not([disabled]){background-color:hsla(213,12%,27%,1);border-color:#636e7b;}/*!sc*/
.cIsLoD[aria-expanded=true]{background-color:hsla(213,12%,27%,1);border-color:#636e7b;}/*!sc*/
.cIsLoD [data-component="leadingVisual"],.cIsLoD [data-component="trailingVisual"],.cIsLoD [data-component="trailingAction"]{color:var(--button-color,#768390);}/*!sc*/
.cIsLoD[data-no-visuals]{color:#636e7b;font-size:14px;font-weight:400;-webkit-flex-shrink:0;-ms-flex-negative:0;flex-shrink:0;border-top-left-radius:0;border-bottom-left-radius:0;}/*!sc*/
.jyKsKT{border-radius:6px;border:1px solid;border-color:rgba(205,217,229,0.1);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#adbac7;background-color:#373e47;box-shadow:0 0 transparent,0 0 transparent;}/*!sc*/
.jyKsKT:focus:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.jyKsKT:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.jyKsKT:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.jyKsKT[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.jyKsKT[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.jyKsKT:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.jyKsKT:active{-webkit-transition:none;transition:none;}/*!sc*/
.jyKsKT:disabled{cursor:not-allowed;box-shadow:none;color:#545d68;}/*!sc*/
.jyKsKT:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.jyKsKT:focus{outline:solid 1px transparent;}}/*!sc*/
.jyKsKT [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.jyKsKT[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.jyKsKT[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.jyKsKT[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.jyKsKT[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.jyKsKT[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.jyKsKT[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.jyKsKT[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.jyKsKT[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.jyKsKT[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.jyKsKT[data-block="block"]{width:100%;}/*!sc*/
.jyKsKT [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.jyKsKT [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.jyKsKT [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.jyKsKT [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.jyKsKT [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.jyKsKT [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.jyKsKT:hover:not([disabled]){background-color:#444c56;border-color:#768390;}/*!sc*/
.jyKsKT:active:not([disabled]){background-color:hsla(213,12%,27%,1);border-color:#636e7b;}/*!sc*/
.jyKsKT[aria-expanded=true]{background-color:hsla(213,12%,27%,1);border-color:#636e7b;}/*!sc*/
.jyKsKT [data-component="leadingVisual"],.jyKsKT [data-component="trailingVisual"],.jyKsKT [data-component="trailingAction"]{color:var(--button-color,#768390);}/*!sc*/
.jyKsKT{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;}/*!sc*/
.jyKsKT svg{color:#768390;}/*!sc*/
.jyKsKT > span{width:inherit;}/*!sc*/
.btfozg{border-radius:6px;border:1px solid;border-color:rgba(205,217,229,0.1);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#adbac7;background-color:#373e47;box-shadow:0 0 transparent,0 0 transparent;}/*!sc*/
.btfozg:focus:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.btfozg:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.btfozg:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.btfozg[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.btfozg[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.btfozg:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.btfozg:active{-webkit-transition:none;transition:none;}/*!sc*/
.btfozg:disabled{cursor:not-allowed;box-shadow:none;color:#545d68;}/*!sc*/
.btfozg:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.btfozg:focus{outline:solid 1px transparent;}}/*!sc*/
.btfozg [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.btfozg[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.btfozg[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.btfozg[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.btfozg[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.btfozg[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.btfozg[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.btfozg[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.btfozg[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.btfozg[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.btfozg[data-block="block"]{width:100%;}/*!sc*/
.btfozg [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.btfozg [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.btfozg [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.btfozg [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.btfozg [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.btfozg [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.btfozg:hover:not([disabled]){background-color:#444c56;border-color:#768390;}/*!sc*/
.btfozg:active:not([disabled]){background-color:hsla(213,12%,27%,1);border-color:#636e7b;}/*!sc*/
.btfozg[aria-expanded=true]{background-color:hsla(213,12%,27%,1);border-color:#636e7b;}/*!sc*/
.btfozg [data-component="leadingVisual"],.btfozg [data-component="trailingVisual"],.btfozg [data-component="trailingAction"]{color:var(--button-color,#768390);}/*!sc*/
.btfozg[data-no-visuals]{border-top-left-radius:0;border-bottom-left-radius:0;display:none;}/*!sc*/
.iflFHp{border-radius:6px;border:1px solid;border-color:rgba(205,217,229,0.1);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#adbac7;background-color:#373e47;box-shadow:0 0 transparent,0 0 transparent;}/*!sc*/
.iflFHp:focus:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.iflFHp:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.iflFHp:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.iflFHp[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.iflFHp[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.iflFHp:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.iflFHp:active{-webkit-transition:none;transition:none;}/*!sc*/
.iflFHp:disabled{cursor:not-allowed;box-shadow:none;color:#545d68;}/*!sc*/
.iflFHp:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.iflFHp:focus{outline:solid 1px transparent;}}/*!sc*/
.iflFHp [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.iflFHp[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.iflFHp[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.iflFHp[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.iflFHp[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.iflFHp[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.iflFHp[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.iflFHp[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.iflFHp[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.iflFHp[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.iflFHp[data-block="block"]{width:100%;}/*!sc*/
.iflFHp [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.iflFHp [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.iflFHp [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.iflFHp [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.iflFHp [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.iflFHp [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.iflFHp:hover:not([disabled]){background-color:#444c56;border-color:#768390;}/*!sc*/
.iflFHp:active:not([disabled]){background-color:hsla(213,12%,27%,1);border-color:#636e7b;}/*!sc*/
.iflFHp[aria-expanded=true]{background-color:hsla(213,12%,27%,1);border-color:#636e7b;}/*!sc*/
.iflFHp [data-component="leadingVisual"],.iflFHp [data-component="trailingVisual"],.iflFHp [data-component="trailingAction"]{color:var(--button-color,#768390);}/*!sc*/
.iflFHp[data-no-visuals]{color:#768390;}/*!sc*/
.degAHJ{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#539bf5;background-color:transparent;box-shadow:none;}/*!sc*/
.degAHJ:focus:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.degAHJ:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.degAHJ:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.degAHJ[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.degAHJ[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.degAHJ:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.degAHJ:active{-webkit-transition:none;transition:none;}/*!sc*/
.degAHJ:disabled{cursor:not-allowed;box-shadow:none;color:#545d68;}/*!sc*/
.degAHJ:disabled [data-component=ButtonCounter],.degAHJ:disabled [data-component="leadingVisual"],.degAHJ:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.degAHJ:focus{outline:solid 1px transparent;}}/*!sc*/
.degAHJ [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.degAHJ[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.degAHJ[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.degAHJ[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.degAHJ[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.degAHJ[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.degAHJ[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.degAHJ[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.degAHJ[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.degAHJ[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.degAHJ[data-block="block"]{width:100%;}/*!sc*/
.degAHJ [data-component="leadingVisual"]{grid-area:leadingVisual;color:#768390;}/*!sc*/
.degAHJ [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.degAHJ [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.degAHJ [data-component="trailingAction"]{margin-right:-4px;color:#768390;}/*!sc*/
.degAHJ [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.degAHJ [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.degAHJ:hover:not([disabled]){background-color:#444c56;}/*!sc*/
.degAHJ:active:not([disabled]){background-color:#2d333b;}/*!sc*/
.degAHJ[aria-expanded=true]{background-color:#2d333b;}/*!sc*/
.degAHJ[data-component="IconButton"][data-no-visuals]{color:#768390;}/*!sc*/
.degAHJ[data-no-visuals]{color:#539bf5;}/*!sc*/
.degAHJ:has([data-component="ButtonCounter"]){color:#539bf5;}/*!sc*/
.degAHJ:disabled[data-no-visuals]{color:#545d68;}/*!sc*/
.degAHJ:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.degAHJ[data-size="small"][data-no-visuals]{margin-left:8px;}/*!sc*/
.fUlRWz{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#adbac7;background-color:transparent;box-shadow:none;}/*!sc*/
.fUlRWz:focus:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.fUlRWz:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.fUlRWz:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.fUlRWz[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.fUlRWz[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.fUlRWz:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.fUlRWz:active{-webkit-transition:none;transition:none;}/*!sc*/
.fUlRWz:disabled{cursor:not-allowed;box-shadow:none;color:#545d68;}/*!sc*/
.fUlRWz:disabled [data-component=ButtonCounter],.fUlRWz:disabled [data-component="leadingVisual"],.fUlRWz:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.fUlRWz:focus{outline:solid 1px transparent;}}/*!sc*/
.fUlRWz [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.fUlRWz[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.fUlRWz[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.fUlRWz[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.fUlRWz[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.fUlRWz[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.fUlRWz[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.fUlRWz[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.fUlRWz[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.fUlRWz[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.fUlRWz[data-block="block"]{width:100%;}/*!sc*/
.fUlRWz [data-component="leadingVisual"]{grid-area:leadingVisual;color:#768390;}/*!sc*/
.fUlRWz [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.fUlRWz [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.fUlRWz [data-component="trailingAction"]{margin-right:-4px;color:#768390;}/*!sc*/
.fUlRWz [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.fUlRWz [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.fUlRWz:hover:not([disabled]){background-color:#444c56;-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.fUlRWz:active:not([disabled]){background-color:#2d333b;-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.fUlRWz[aria-expanded=true]{background-color:#2d333b;}/*!sc*/
.fUlRWz[data-component="IconButton"][data-no-visuals]{color:#768390;}/*!sc*/
.fUlRWz[data-no-visuals]{color:#539bf5;}/*!sc*/
.fUlRWz:has([data-component="ButtonCounter"]){color:#539bf5;}/*!sc*/
.fUlRWz:disabled[data-no-visuals]{color:#545d68;}/*!sc*/
.fUlRWz:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.fUlRWz:focus:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.hhwrXY{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#539bf5;background-color:transparent;box-shadow:none;}/*!sc*/
.hhwrXY:focus:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.hhwrXY:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.hhwrXY:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.hhwrXY[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.hhwrXY[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.hhwrXY:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.hhwrXY:active{-webkit-transition:none;transition:none;}/*!sc*/
.hhwrXY:disabled{cursor:not-allowed;box-shadow:none;color:#545d68;}/*!sc*/
.hhwrXY:disabled [data-component=ButtonCounter],.hhwrXY:disabled [data-component="leadingVisual"],.hhwrXY:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.hhwrXY:focus{outline:solid 1px transparent;}}/*!sc*/
.hhwrXY [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.hhwrXY[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.hhwrXY[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;color:#adbac7;margin-left:8px;}/*!sc*/
.hhwrXY[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.hhwrXY[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.hhwrXY[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.hhwrXY[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.hhwrXY[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.hhwrXY[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.hhwrXY[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.hhwrXY[data-block="block"]{width:100%;}/*!sc*/
.hhwrXY [data-component="leadingVisual"]{grid-area:leadingVisual;color:#768390;}/*!sc*/
.hhwrXY [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.hhwrXY [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.hhwrXY [data-component="trailingAction"]{margin-right:-4px;color:#768390;}/*!sc*/
.hhwrXY [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.hhwrXY [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.hhwrXY:hover:not([disabled]){background-color:#444c56;}/*!sc*/
.hhwrXY:active:not([disabled]){background-color:#2d333b;}/*!sc*/
.hhwrXY[aria-expanded=true]{background-color:#2d333b;}/*!sc*/
.hhwrXY[data-component="IconButton"][data-no-visuals]{color:#768390;}/*!sc*/
.hhwrXY[data-no-visuals]{color:#539bf5;}/*!sc*/
.hhwrXY:has([data-component="ButtonCounter"]){color:#539bf5;}/*!sc*/
.hhwrXY:disabled[data-no-visuals]{color:#545d68;}/*!sc*/
.hhwrXY:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.fRleic{border-radius:6px;border:1px solid;border-color:rgba(205,217,229,0.1);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#adbac7;background-color:#373e47;box-shadow:0 0 transparent,0 0 transparent;padding-left:8px;padding-right:8px;}/*!sc*/
.fRleic:focus:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.fRleic:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.fRleic:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.fRleic[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.fRleic[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.fRleic:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.fRleic:active{-webkit-transition:none;transition:none;}/*!sc*/
.fRleic:disabled{cursor:not-allowed;box-shadow:none;color:#545d68;}/*!sc*/
.fRleic:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.fRleic:focus{outline:solid 1px transparent;}}/*!sc*/
.fRleic [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.fRleic[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.fRleic[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.fRleic[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.fRleic[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.fRleic[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.fRleic[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.fRleic[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.fRleic[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.fRleic[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.fRleic[data-block="block"]{width:100%;}/*!sc*/
.fRleic [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.fRleic [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.fRleic [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.fRleic [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.fRleic [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.fRleic [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.fRleic:hover:not([disabled]){background-color:#444c56;border-color:#768390;}/*!sc*/
.fRleic:active:not([disabled]){background-color:hsla(213,12%,27%,1);border-color:#636e7b;}/*!sc*/
.fRleic[aria-expanded=true]{background-color:hsla(213,12%,27%,1);border-color:#636e7b;}/*!sc*/
.fRleic [data-component="leadingVisual"],.fRleic [data-component="trailingVisual"],.fRleic [data-component="trailingAction"]{color:var(--button-color,#768390);}/*!sc*/
.fRleic linkButtonSx:hover:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.fRleic linkButtonSx:focus:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.fRleic linkButtonSx:active:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.iclSHR{border-radius:6px;border:1px solid;border-color:rgba(205,217,229,0.1);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#adbac7;background-color:#373e47;box-shadow:0 0 transparent,0 0 transparent;}/*!sc*/
.iclSHR:focus:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.iclSHR:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.iclSHR:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.iclSHR[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.iclSHR[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.iclSHR:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.iclSHR:active{-webkit-transition:none;transition:none;}/*!sc*/
.iclSHR:disabled{cursor:not-allowed;box-shadow:none;color:#545d68;}/*!sc*/
.iclSHR:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.iclSHR:focus{outline:solid 1px transparent;}}/*!sc*/
.iclSHR [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.iclSHR[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.iclSHR[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.iclSHR[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.iclSHR[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.iclSHR[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.iclSHR[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.iclSHR[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.iclSHR[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.iclSHR[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.iclSHR[data-block="block"]{width:100%;}/*!sc*/
.iclSHR [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.iclSHR [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.iclSHR [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.iclSHR [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.iclSHR [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.iclSHR [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.iclSHR:hover:not([disabled]){background-color:#444c56;border-color:#768390;}/*!sc*/
.iclSHR:active:not([disabled]){background-color:hsla(213,12%,27%,1);border-color:#636e7b;}/*!sc*/
.iclSHR[aria-expanded=true]{background-color:hsla(213,12%,27%,1);border-color:#636e7b;}/*!sc*/
.iclSHR [data-component="leadingVisual"],.iclSHR [data-component="trailingVisual"],.iclSHR [data-component="trailingAction"]{color:var(--button-color,#768390);}/*!sc*/
.bykEZB{border-radius:6px;border:1px solid;border-color:rgba(205,217,229,0.1);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#adbac7;background-color:#373e47;box-shadow:0 0 transparent,0 0 transparent;}/*!sc*/
.bykEZB:focus:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.bykEZB:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.bykEZB:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.bykEZB[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.bykEZB[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.bykEZB:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.bykEZB:active{-webkit-transition:none;transition:none;}/*!sc*/
.bykEZB:disabled{cursor:not-allowed;box-shadow:none;color:#545d68;}/*!sc*/
.bykEZB:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.bykEZB:focus{outline:solid 1px transparent;}}/*!sc*/
.bykEZB [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.bykEZB[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.bykEZB[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.bykEZB[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.bykEZB[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.bykEZB[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.bykEZB[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.bykEZB[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.bykEZB[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.bykEZB[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.bykEZB[data-block="block"]{width:100%;}/*!sc*/
.bykEZB [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.bykEZB [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.bykEZB [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.bykEZB [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.bykEZB [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.bykEZB [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.bykEZB:hover:not([disabled]){background-color:#444c56;border-color:#768390;}/*!sc*/
.bykEZB:active:not([disabled]){background-color:hsla(213,12%,27%,1);border-color:#636e7b;}/*!sc*/
.bykEZB[aria-expanded=true]{background-color:hsla(213,12%,27%,1);border-color:#636e7b;}/*!sc*/
.bykEZB [data-component="leadingVisual"],.bykEZB [data-component="trailingVisual"],.bykEZB [data-component="trailingAction"]{color:var(--button-color,#768390);}/*!sc*/
.bykEZB[data-size="small"][data-no-visuals]{border-top-left-radius:0;border-bottom-left-radius:0;}/*!sc*/
.iEfBoP{border-radius:6px;border:1px solid;border-color:rgba(205,217,229,0.1);font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#adbac7;background-color:#373e47;box-shadow:0 0 transparent,0 0 transparent;}/*!sc*/
.iEfBoP:focus:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.iEfBoP:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.iEfBoP:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.iEfBoP[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.iEfBoP[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.iEfBoP:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.iEfBoP:active{-webkit-transition:none;transition:none;}/*!sc*/
.iEfBoP:disabled{cursor:not-allowed;box-shadow:none;color:#545d68;}/*!sc*/
.iEfBoP:disabled [data-component=ButtonCounter]{color:inherit;}/*!sc*/
@media (forced-colors:active){.iEfBoP:focus{outline:solid 1px transparent;}}/*!sc*/
.iEfBoP [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.iEfBoP[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.iEfBoP[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.iEfBoP[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.iEfBoP[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.iEfBoP[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.iEfBoP[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.iEfBoP[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.iEfBoP[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.iEfBoP[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.iEfBoP[data-block="block"]{width:100%;}/*!sc*/
.iEfBoP [data-component="leadingVisual"]{grid-area:leadingVisual;}/*!sc*/
.iEfBoP [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.iEfBoP [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.iEfBoP [data-component="trailingAction"]{margin-right:-4px;}/*!sc*/
.iEfBoP [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.iEfBoP [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.iEfBoP:hover:not([disabled]){background-color:#444c56;border-color:#768390;}/*!sc*/
.iEfBoP:active:not([disabled]){background-color:hsla(213,12%,27%,1);border-color:#636e7b;}/*!sc*/
.iEfBoP[aria-expanded=true]{background-color:hsla(213,12%,27%,1);border-color:#636e7b;}/*!sc*/
.iEfBoP [data-component="leadingVisual"],.iEfBoP [data-component="trailingVisual"],.iEfBoP [data-component="trailingAction"]{color:var(--button-color,#768390);}/*!sc*/
.iEfBoP[data-size="small"][data-no-visuals]{border-top-right-radius:0;border-bottom-right-radius:0;border-right-width:0;}/*!sc*/
.iEfBoP[data-size="small"][data-no-visuals]:hover:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.iEfBoP[data-size="small"][data-no-visuals]:focus:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.iEfBoP[data-size="small"][data-no-visuals]:active:not([disabled]){-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.iajnCX{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#539bf5;background-color:transparent;box-shadow:none;}/*!sc*/
.iajnCX:focus:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.iajnCX:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.iajnCX:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.iajnCX[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.iajnCX[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.iajnCX:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.iajnCX:active{-webkit-transition:none;transition:none;}/*!sc*/
.iajnCX:disabled{cursor:not-allowed;box-shadow:none;color:#545d68;}/*!sc*/
.iajnCX:disabled [data-component=ButtonCounter],.iajnCX:disabled [data-component="leadingVisual"],.iajnCX:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.iajnCX:focus{outline:solid 1px transparent;}}/*!sc*/
.iajnCX [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.iajnCX[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.iajnCX[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.iajnCX[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.iajnCX[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.iajnCX[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.iajnCX[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.iajnCX[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.iajnCX[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.iajnCX[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.iajnCX[data-block="block"]{width:100%;}/*!sc*/
.iajnCX [data-component="leadingVisual"]{grid-area:leadingVisual;color:#768390;}/*!sc*/
.iajnCX [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.iajnCX [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.iajnCX [data-component="trailingAction"]{margin-right:-4px;color:#768390;}/*!sc*/
.iajnCX [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.iajnCX [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.iajnCX:hover:not([disabled]){background-color:#444c56;}/*!sc*/
.iajnCX:active:not([disabled]){background-color:#2d333b;}/*!sc*/
.iajnCX[aria-expanded=true]{background-color:#2d333b;}/*!sc*/
.iajnCX[data-component="IconButton"][data-no-visuals]{color:#768390;}/*!sc*/
.iajnCX[data-no-visuals]{color:#539bf5;}/*!sc*/
.iajnCX:has([data-component="ButtonCounter"]){color:#539bf5;}/*!sc*/
.iajnCX:disabled[data-no-visuals]{color:#545d68;}/*!sc*/
.iajnCX:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.iajnCX[data-size="small"][data-no-visuals]{color:var(--fgColor-muted,var(--color-fg-muted));margin-right:8px;}/*!sc*/
.grSsTo{border-radius:6px;border:1px solid;border-color:transparent;font-family:inherit;font-weight:500;font-size:14px;cursor:pointer;-webkit-appearance:none;-moz-appearance:none;appearance:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-text-decoration:none;text-decoration:none;text-align:center;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;height:32px;padding:0 12px;gap:8px;min-width:-webkit-max-content;min-width:-moz-max-content;min-width:max-content;-webkit-transition:80ms cubic-bezier(0.65,0,0.35,1);transition:80ms cubic-bezier(0.65,0,0.35,1);-webkit-transition-property:color,fill,background-color,border-color;transition-property:color,fill,background-color,border-color;color:#539bf5;background-color:transparent;box-shadow:none;}/*!sc*/
.grSsTo:focus:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.grSsTo:focus:not(:disabled):not(:focus-visible){outline:solid 1px transparent;}/*!sc*/
.grSsTo:focus-visible:not(:disabled){box-shadow:none;outline:2px solid #539bf5;outline-offset:-2px;}/*!sc*/
.grSsTo[href]{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;}/*!sc*/
.grSsTo[href]:hover{-webkit-text-decoration:none;text-decoration:none;}/*!sc*/
.grSsTo:hover{-webkit-transition-duration:80ms;transition-duration:80ms;}/*!sc*/
.grSsTo:active{-webkit-transition:none;transition:none;}/*!sc*/
.grSsTo:disabled{cursor:not-allowed;box-shadow:none;color:#545d68;}/*!sc*/
.grSsTo:disabled [data-component=ButtonCounter],.grSsTo:disabled [data-component="leadingVisual"],.grSsTo:disabled [data-component="trailingAction"]{color:inherit;}/*!sc*/
@media (forced-colors:active){.grSsTo:focus{outline:solid 1px transparent;}}/*!sc*/
.grSsTo [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.grSsTo[data-component=IconButton]{display:inline-grid;padding:unset;place-content:center;width:32px;min-width:unset;}/*!sc*/
.grSsTo[data-size="small"]{padding:0 8px;height:28px;gap:4px;font-size:12px;}/*!sc*/
.grSsTo[data-size="small"] [data-component="text"]{line-height:calc(20 / 12);}/*!sc*/
.grSsTo[data-size="small"] [data-component=ButtonCounter]{font-size:12px;}/*!sc*/
.grSsTo[data-size="small"] [data-component="buttonContent"] > :not(:last-child){margin-right:4px;}/*!sc*/
.grSsTo[data-size="small"][data-component=IconButton]{width:28px;padding:unset;}/*!sc*/
.grSsTo[data-size="large"]{padding:0 16px;height:40px;gap:8px;}/*!sc*/
.grSsTo[data-size="large"] [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.grSsTo[data-size="large"][data-component=IconButton]{width:40px;padding:unset;}/*!sc*/
.grSsTo[data-block="block"]{width:100%;}/*!sc*/
.grSsTo [data-component="leadingVisual"]{grid-area:leadingVisual;color:#768390;}/*!sc*/
.grSsTo [data-component="text"]{grid-area:text;line-height:calc(20/14);white-space:nowrap;}/*!sc*/
.grSsTo [data-component="trailingVisual"]{grid-area:trailingVisual;}/*!sc*/
.grSsTo [data-component="trailingAction"]{margin-right:-4px;color:#768390;}/*!sc*/
.grSsTo [data-component="buttonContent"]{-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;display:grid;grid-template-areas:"leadingVisual text trailingVisual";grid-template-columns:min-content minmax(0,auto) min-content;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-align-content:center;-ms-flex-line-pack:center;align-content:center;}/*!sc*/
.grSsTo [data-component="buttonContent"] > :not(:last-child){margin-right:8px;}/*!sc*/
.grSsTo:hover:not([disabled]){background-color:#444c56;}/*!sc*/
.grSsTo:active:not([disabled]){background-color:#2d333b;}/*!sc*/
.grSsTo[aria-expanded=true]{background-color:#2d333b;}/*!sc*/
.grSsTo[data-component="IconButton"][data-no-visuals]{color:#768390;}/*!sc*/
.grSsTo[data-no-visuals]{color:#539bf5;}/*!sc*/
.grSsTo:has([data-component="ButtonCounter"]){color:#539bf5;}/*!sc*/
.grSsTo:disabled[data-no-visuals]{color:#545d68;}/*!sc*/
.grSsTo:disabled[data-no-visuals] [data-component=ButtonCounter]{color:inherit;}/*!sc*/
.grSsTo[data-size="small"][data-no-visuals]{color:#768390;}/*!sc*/
data-styled.g28[id="types__StyledButton-sc-ws60qy-0"]{content:"bWtVmw,imyHbr,eJRzxr,eCoUah,cIsLoD,jyKsKT,btfozg,iflFHp,degAHJ,fUlRWz,hhwrXY,fRleic,iclSHR,bykEZB,iEfBoP,iajnCX,grSsTo,"}/*!sc*/
.iSGYLp{position:relative;display:inline-block;}/*!sc*/
.iSGYLp::before{position:absolute;z-index:1000001;display:none;width:0px;height:0px;color:#636e7b;pointer-events:none;content:'';border:6px solid transparent;opacity:0;}/*!sc*/
.iSGYLp::after{position:absolute;z-index:1000000;display:none;padding:0.5em 0.75em;font:normal normal 11px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji";-webkit-font-smoothing:subpixel-antialiased;color:#cdd9e5;text-align:center;-webkit-text-decoration:none;text-decoration:none;text-shadow:none;text-transform:none;-webkit-letter-spacing:normal;-moz-letter-spacing:normal;-ms-letter-spacing:normal;letter-spacing:normal;word-wrap:break-word;white-space:pre;pointer-events:none;content:attr(aria-label);background:#636e7b;border-radius:3px;opacity:0;}/*!sc*/
@-webkit-keyframes tooltip-appear{from{opacity:0;}to{opacity:1;}}/*!sc*/
@keyframes tooltip-appear{from{opacity:0;}to{opacity:1;}}/*!sc*/
.iSGYLp:hover::before,.iSGYLp:active::before,.iSGYLp:focus::before,.iSGYLp:focus-within::before,.iSGYLp:hover::after,.iSGYLp:active::after,.iSGYLp:focus::after,.iSGYLp:focus-within::after{display:inline-block;-webkit-text-decoration:none;text-decoration:none;-webkit-animation-name:tooltip-appear;animation-name:tooltip-appear;-webkit-animation-duration:0.1s;animation-duration:0.1s;-webkit-animation-fill-mode:forwards;animation-fill-mode:forwards;-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in;-webkit-animation-delay:0.4s;animation-delay:0.4s;}/*!sc*/
.iSGYLp.tooltipped-no-delay:hover::before,.iSGYLp.tooltipped-no-delay:active::before,.iSGYLp.tooltipped-no-delay:focus::before,.iSGYLp.tooltipped-no-delay:focus-within::before,.iSGYLp.tooltipped-no-delay:hover::after,.iSGYLp.tooltipped-no-delay:active::after,.iSGYLp.tooltipped-no-delay:focus::after,.iSGYLp.tooltipped-no-delay:focus-within::after{-webkit-animation-delay:0s;animation-delay:0s;}/*!sc*/
.iSGYLp.tooltipped-multiline:hover::after,.iSGYLp.tooltipped-multiline:active::after,.iSGYLp.tooltipped-multiline:focus::after,.iSGYLp.tooltipped-multiline:focus-within::after{display:table-cell;}/*!sc*/
.iSGYLp.tooltipped-s::after,.iSGYLp.tooltipped-se::after,.iSGYLp.tooltipped-sw::after{top:100%;right:50%;margin-top:6px;}/*!sc*/
.iSGYLp.tooltipped-s::before,.iSGYLp.tooltipped-se::before,.iSGYLp.tooltipped-sw::before{top:auto;right:50%;bottom:-7px;margin-right:-6px;border-bottom-color:#636e7b;}/*!sc*/
.iSGYLp.tooltipped-se::after{right:auto;left:50%;margin-left:-16px;}/*!sc*/
.iSGYLp.tooltipped-sw::after{margin-right:-16px;}/*!sc*/
.iSGYLp.tooltipped-n::after,.iSGYLp.tooltipped-ne::after,.iSGYLp.tooltipped-nw::after{right:50%;bottom:100%;margin-bottom:6px;}/*!sc*/
.iSGYLp.tooltipped-n::before,.iSGYLp.tooltipped-ne::before,.iSGYLp.tooltipped-nw::before{top:-7px;right:50%;bottom:auto;margin-right:-6px;border-top-color:#636e7b;}/*!sc*/
.iSGYLp.tooltipped-ne::after{right:auto;left:50%;margin-left:-16px;}/*!sc*/
.iSGYLp.tooltipped-nw::after{margin-right:-16px;}/*!sc*/
.iSGYLp.tooltipped-s::after,.iSGYLp.tooltipped-n::after{-webkit-transform:translateX(50%);-ms-transform:translateX(50%);transform:translateX(50%);}/*!sc*/
.iSGYLp.tooltipped-w::after{right:100%;bottom:50%;margin-right:6px;-webkit-transform:translateY(50%);-ms-transform:translateY(50%);transform:translateY(50%);}/*!sc*/
.iSGYLp.tooltipped-w::before{top:50%;bottom:50%;left:-7px;margin-top:-6px;border-left-color:#636e7b;}/*!sc*/
.iSGYLp.tooltipped-e::after{bottom:50%;left:100%;margin-left:6px;-webkit-transform:translateY(50%);-ms-transform:translateY(50%);transform:translateY(50%);}/*!sc*/
.iSGYLp.tooltipped-e::before{top:50%;right:-7px;bottom:50%;margin-top:-6px;border-right-color:#636e7b;}/*!sc*/
.iSGYLp.tooltipped-multiline::after{width:-webkit-max-content;width:-moz-max-content;width:max-content;max-width:250px;word-wrap:break-word;white-space:pre-line;border-collapse:separate;}/*!sc*/
.iSGYLp.tooltipped-multiline.tooltipped-s::after,.iSGYLp.tooltipped-multiline.tooltipped-n::after{right:auto;left:50%;-webkit-transform:translateX(-50%);-ms-transform:translateX(-50%);transform:translateX(-50%);}/*!sc*/
.iSGYLp.tooltipped-multiline.tooltipped-w::after,.iSGYLp.tooltipped-multiline.tooltipped-e::after{right:100%;}/*!sc*/
.iSGYLp.tooltipped-align-right-2::after{right:0;margin-right:0;}/*!sc*/
.iSGYLp.tooltipped-align-right-2::before{right:15px;}/*!sc*/
.iSGYLp.tooltipped-align-left-2::after{left:0;margin-left:0;}/*!sc*/
.iSGYLp.tooltipped-align-left-2::before{left:10px;}/*!sc*/
data-styled.g29[id="Tooltip__TooltipBase-sc-uha8qm-0"]{content:"iSGYLp,"}/*!sc*/
.cDLBls{border:0;font-size:inherit;font-family:inherit;background-color:transparent;-webkit-appearance:none;color:inherit;width:100%;}/*!sc*/
.cDLBls:focus{outline:0;}/*!sc*/
data-styled.g30[id="UnstyledTextInput-sc-14ypya-0"]{content:"cDLBls,"}/*!sc*/
.bOMzPg{min-width:0;}/*!sc*/
.kvpHZx{padding-left:4px;padding-right:4px;font-weight:400;color:#768390;font-size:16px;}/*!sc*/
.djgCKN{color:#adbac7;}/*!sc*/
.kpJgoj{padding-left:4px;padding-right:4px;font-weight:400;color:#768390;font-size:14px;}/*!sc*/
data-styled.g36[id="Text-sc-17v1xeu-0"]{content:"bOMzPg,kvpHZx,djgCKN,gPDEWA,kpJgoj,"}/*!sc*/
.cjbBGq{display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;vertical-align:middle;isolation:isolate;}/*!sc*/
.cjbBGq.cjbBGq > *{margin-inline-end:-1px;position:relative;border-radius:0;}/*!sc*/
.cjbBGq.cjbBGq > *:first-child{border-top-left-radius:6px;border-bottom-left-radius:6px;}/*!sc*/
.cjbBGq.cjbBGq > *:last-child{border-top-right-radius:6px;border-bottom-right-radius:6px;}/*!sc*/
.cjbBGq.cjbBGq > *:focus,.cjbBGq.cjbBGq > *:active,.cjbBGq.cjbBGq > *:hover{z-index:1;}/*!sc*/
data-styled.g67[id="ButtonGroup-sc-1gxhls1-0"]{content:"cjbBGq,"}/*!sc*/
.kcTGcx{--segmented-control-button-inner-padding:12px;--segmented-control-button-bg-inset:4px;--segmented-control-outer-radius:6px;background-color:transparent;border-color:transparent;border-radius:var(--segmented-control-outer-radius);border-width:0;color:currentColor;cursor:pointer;font-family:inherit;font-size:inherit;font-weight:600;padding:0;height:100%;width:100%;}/*!sc*/
.kcTGcx .segmentedControl-content{-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;background-color:#22272e;border-color:#636e7b;border-style:solid;border-width:1px;border-radius:var(--segmented-control-outer-radius);display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;height:100%;-webkit-box-pack:center;-webkit-justify-content:center;-ms-flex-pack:center;justify-content:center;padding-left:var(--segmented-control-button-inner-padding);padding-right:var(--segmented-control-button-inner-padding);}/*!sc*/
.kcTGcx svg{fill:#768390;}/*!sc*/
.kcTGcx:focus:focus-visible:not(:last-child):after{width:0;}/*!sc*/
.kcTGcx .segmentedControl-text:after{content:"Preview";display:block;font-weight:600;height:0;overflow:hidden;pointer-events:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;visibility:hidden;}/*!sc*/
@media (pointer:coarse){.kcTGcx:before{content:"";position:absolute;left:0;right:0;-webkit-transform:translateY(-50%);-ms-transform:translateY(-50%);transform:translateY(-50%);top:50%;min-height:44px;}}/*!sc*/
.WHXNM{--segmented-control-button-inner-padding:12px;--segmented-control-button-bg-inset:4px;--segmented-control-outer-radius:6px;background-color:transparent;border-color:transparent;border-radius:var(--segmented-control-outer-radius);border-width:0;color:currentColor;cursor:pointer;font-family:inherit;font-size:inherit;font-weight:400;padding:var(--segmented-control-button-bg-inset);height:100%;width:100%;}/*!sc*/
.WHXNM .segmentedControl-content{-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;background-color:transparent;border-color:transparent;border-style:solid;border-width:1px;border-radius:calc(var(--segmented-control-outer-radius) - var(--segmented-control-button-bg-inset) / 2);display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;height:100%;-webkit-box-pack:center;-webkit-justify-content:center;-ms-flex-pack:center;justify-content:center;padding-left:calc(var(--segmented-control-button-inner-padding) - var(--segmented-control-button-bg-inset));padding-right:calc(var(--segmented-control-button-inner-padding) - var(--segmented-control-button-bg-inset));}/*!sc*/
.WHXNM svg{fill:#768390;}/*!sc*/
.WHXNM:hover .segmentedControl-content{background-color:#444c56;}/*!sc*/
.WHXNM:active .segmentedControl-content{background-color:#373e47;}/*!sc*/
.WHXNM:focus:focus-visible:not(:last-child):after{width:0;}/*!sc*/
.WHXNM .segmentedControl-text:after{content:"Code";display:block;font-weight:600;height:0;overflow:hidden;pointer-events:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;visibility:hidden;}/*!sc*/
@media (pointer:coarse){.WHXNM:before{content:"";position:absolute;left:0;right:0;-webkit-transform:translateY(-50%);-ms-transform:translateY(-50%);transform:translateY(-50%);top:50%;min-height:44px;}}/*!sc*/
.iQDmCy{--segmented-control-button-inner-padding:12px;--segmented-control-button-bg-inset:4px;--segmented-control-outer-radius:6px;background-color:transparent;border-color:transparent;border-radius:var(--segmented-control-outer-radius);border-width:0;color:currentColor;cursor:pointer;font-family:inherit;font-size:inherit;font-weight:400;padding:var(--segmented-control-button-bg-inset);height:100%;width:100%;}/*!sc*/
.iQDmCy .segmentedControl-content{-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;background-color:transparent;border-color:transparent;border-style:solid;border-width:1px;border-radius:calc(var(--segmented-control-outer-radius) - var(--segmented-control-button-bg-inset) / 2);display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;height:100%;-webkit-box-pack:center;-webkit-justify-content:center;-ms-flex-pack:center;justify-content:center;padding-left:calc(var(--segmented-control-button-inner-padding) - var(--segmented-control-button-bg-inset));padding-right:calc(var(--segmented-control-button-inner-padding) - var(--segmented-control-button-bg-inset));}/*!sc*/
.iQDmCy svg{fill:#768390;}/*!sc*/
.iQDmCy:hover .segmentedControl-content{background-color:#444c56;}/*!sc*/
.iQDmCy:active .segmentedControl-content{background-color:#373e47;}/*!sc*/
.iQDmCy:focus:focus-visible:not(:last-child):after{width:0;}/*!sc*/
.iQDmCy .segmentedControl-text:after{content:"Blame";display:block;font-weight:600;height:0;overflow:hidden;pointer-events:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;visibility:hidden;}/*!sc*/
@media (pointer:coarse){.iQDmCy:before{content:"";position:absolute;left:0;right:0;-webkit-transform:translateY(-50%);-ms-transform:translateY(-50%);transform:translateY(-50%);top:50%;min-height:44px;}}/*!sc*/
data-styled.g91[id="SegmentedControlButton__SegmentedControlButtonStyled-sc-8lkgxl-0"]{content:"kcTGcx,WHXNM,iQDmCy,"}/*!sc*/
.hDkNhA{background-color:rgba(99,110,123,0.1);border-radius:6px;display:-webkit-inline-box;display:-webkit-inline-flex;display:-ms-inline-flexbox;display:inline-flex;font-size:14px;height:28px;margin:0;padding:0;}/*!sc*/
data-styled.g93[id="SegmentedControl__SegmentedControlList-sc-1rzig82-0"]{content:"hDkNhA,"}/*!sc*/
body[data-page-layout-dragging="true"]{cursor:col-resize;}/*!sc*/
body[data-page-layout-dragging="true"] *{-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;}/*!sc*/
data-styled.g97[id="sc-global-gbKrvU1"]{content:"sc-global-gbKrvU1,"}/*!sc*/
.dDkgrC{list-style:none;padding:0;margin:0;}/*!sc*/
.dDkgrC .PRIVATE_TreeView-item{outline:none;}/*!sc*/
.dDkgrC .PRIVATE_TreeView-item:focus-visible > div,.dDkgrC .PRIVATE_TreeView-item.focus-visible > div{box-shadow:inset 0 0 0 2px #539bf5;}/*!sc*/
@media (forced-colors:active){.dDkgrC .PRIVATE_TreeView-item:focus-visible > div,.dDkgrC .PRIVATE_TreeView-item.focus-visible > div{outline:2px solid HighlightText;outline-offset:-2;}}/*!sc*/
.dDkgrC .PRIVATE_TreeView-item-container{--level:1;--toggle-width:1rem;position:relative;display:grid;grid-template-columns:calc(calc(var(--level) - 1) * (var(--toggle-width) / 2)) var(--toggle-width) 1fr;grid-template-areas:'spacer toggle content';width:100%;min-height:2rem;font-size:14px;color:#adbac7;border-radius:6px;cursor:pointer;}/*!sc*/
.dDkgrC .PRIVATE_TreeView-item-container:hover{background-color:rgba(144,157,171,0.12);}/*!sc*/
@media (forced-colors:active){.dDkgrC .PRIVATE_TreeView-item-container:hover{outline:2px solid transparent;outline-offset:-2px;}}/*!sc*/
@media (pointer:coarse){.dDkgrC .PRIVATE_TreeView-item-container{--toggle-width:1.5rem;min-height:2.75rem;}}/*!sc*/
.dDkgrC .PRIVATE_TreeView-item-container:has(.PRIVATE_TreeView-item-skeleton):hover{background-color:transparent;cursor:default;}/*!sc*/
@media (forced-colors:active){.dDkgrC .PRIVATE_TreeView-item-container:has(.PRIVATE_TreeView-item-skeleton):hover{outline:none;}}/*!sc*/
.dDkgrC[data-omit-spacer='true'] .PRIVATE_TreeView-item-container{grid-template-columns:0 0 1fr;}/*!sc*/
.dDkgrC .PRIVATE_TreeView-item[aria-current='true'] > .PRIVATE_TreeView-item-container{background-color:rgba(144,157,171,0.08);}/*!sc*/
.dDkgrC .PRIVATE_TreeView-item[aria-current='true'] > .PRIVATE_TreeView-item-container::after{content:'';position:absolute;top:calc(50% - 0.75rem);left:-8px;width:0.25rem;height:1.5rem;background-color:#539bf5;border-radius:6px;}/*!sc*/
@media (forced-colors:active){.dDkgrC .PRIVATE_TreeView-item[aria-current='true'] > .PRIVATE_TreeView-item-container::after{background-color:HighlightText;}}/*!sc*/
.dDkgrC .PRIVATE_TreeView-item-toggle{grid-area:toggle;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;-ms-flex-pack:center;justify-content:center;height:100%;color:#768390;}/*!sc*/
.dDkgrC .PRIVATE_TreeView-item-toggle--hover:hover{background-color:rgba(144,157,171,0.12);}/*!sc*/
.dDkgrC .PRIVATE_TreeView-item-toggle--end{border-top-left-radius:6px;border-bottom-left-radius:6px;}/*!sc*/
.dDkgrC .PRIVATE_TreeView-item-content{grid-area:content;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;height:100%;padding:0 8px;gap:8px;}/*!sc*/
.dDkgrC .PRIVATE_TreeView-item-content-text{-webkit-flex:1 1 auto;-ms-flex:1 1 auto;flex:1 1 auto;width:0;overflow:hidden;white-space:nowrap;text-overflow:ellipsis;}/*!sc*/
.dDkgrC .PRIVATE_TreeView-item-visual{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;color:#768390;}/*!sc*/
.dDkgrC .PRIVATE_TreeView-item-level-line{width:100%;height:100%;border-right:1px solid;border-color:rgba(205,217,229,0.1);}/*!sc*/
@media (hover:hover){.dDkgrC .PRIVATE_TreeView-item-level-line{border-color:transparent;}.dDkgrC:hover .PRIVATE_TreeView-item-level-line,.dDkgrC:focus-within .PRIVATE_TreeView-item-level-line{border-color:rgba(205,217,229,0.1);}}/*!sc*/
.dDkgrC .PRIVATE_TreeView-directory-icon{display:grid;color:#768390;}/*!sc*/
.dDkgrC .PRIVATE_VisuallyHidden{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;-webkit-clip:rect(0,0,0,0);clip:rect(0,0,0,0);white-space:nowrap;border-width:0;}/*!sc*/
data-styled.g104[id="TreeView__UlBox-sc-4ex6b6-0"]{content:"dDkgrC,"}/*!sc*/
</style><meta data-hydrostats="publish"/> <!-- --> <!-- --> <!-- --> <button hidden="" data-testid="header-permalink-button" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button><div class="Box-sc-g0xbh4-0"><div style="--sticky-pane-height:100vh" class="Box-sc-g0xbh4-0 fSWWem"><div class="Box-sc-g0xbh4-0 kPPmzM"><div class="Box-sc-g0xbh4-0 cIAPDV"><div tabindex="0" class="Box-sc-g0xbh4-0 gvCnwW"><div class="Box-sc-g0xbh4-0 ioxSsX"><div class="Box-sc-g0xbh4-0 eUyHuk"></div><div class="Box-sc-g0xbh4-0 hAeDYA"><div role="separator" class="Box-sc-g0xbh4-0 hYdBkT"></div></div><div style="--pane-width:320px" class="Box-sc-g0xbh4-0 gNdDUH"><span class="_VisuallyHidden__VisuallyHidden-sc-11jhm7a-0 rTZSs"><form><label for=":Rdjal5:-width-input">Pane width</label><p id=":Rdjal5:-input-hint">Use a value between <!-- -->0<!-- -->% and <!-- -->0<!-- -->%</p><input id=":Rdjal5:-width-input" aria-describedby=":Rdjal5:-input-hint" name="pane-width" inputMode="numeric" pattern="[0-9]*" autoCorrect="off" autoComplete="off" type="text" value=""/><button type="submit">Change width</button></form></span><div class="Box-sc-g0xbh4-0 react-tree-pane-contents"><div id="repos-file-tree" class="Box-sc-g0xbh4-0 jywUSN"><div class="Box-sc-g0xbh4-0 hBSSUC"><div class="Box-sc-g0xbh4-0 iPurHz"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 fNPcqd"><button style="--button-color:fg.muted" type="button" aria-label="Expand side panel" data-testid="expand-file-tree-button-mobile" class="types__StyledButton-sc-ws60qy-0 bWtVmw"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-arrow-left" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M7.78 12.53a.75.75 0 0 1-1.06 0L2.47 8.28a.75.75 0 0 1 0-1.06l4.25-4.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L4.81 7h7.44a.75.75 0 0 1 0 1.5H4.81l2.97 2.97a.75.75 0 0 1 0 1.06Z"></path></svg></span><span data-component="text">Files</span></span></button><button data-component="IconButton" type="button" data-testid="collapse-file-tree-button" aria-label="Side panel" aria-expanded="true" aria-controls="repos-file-tree" class="types__StyledButton-sc-ws60qy-0 imyHbr" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-sidebar-expand" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.177 7.823 2.396-2.396A.25.25 0 0 1 7 5.604v4.792a.25.25 0 0 1-.427.177L4.177 8.177a.25.25 0 0 1 0-.354Z"></path><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25H9.5v-13Zm12.5 13a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11v13Z"></path></svg></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button></h2><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 imcwCi">Files</h2></div><div class="Box-sc-g0xbh4-0 hVHHYa"><div class="Box-sc-g0xbh4-0 idZfsJ"><button type="button" id="branch-picker-repos-header-ref-selector" aria-haspopup="true" tabindex="0" aria-label="trunk branch" data-testid="anchor-button" class="types__StyledButton-sc-ws60qy-0 eJRzxr react-repos-tree-pane-ref-selector width-full ref-selector-class"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text"><div class="Box-sc-g0xbh4-0 bKgizp"><div class="Box-sc-g0xbh4-0 fxhqJs"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="Box-sc-g0xbh4-0 caeYDk"><span class="Text-sc-17v1xeu-0 bOMzPg"> <!-- -->trunk</span></div></div></span><span data-component="trailingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><button hidden="" data-hotkey-scope="read-only-cursor-text-area"></button></div><div class="Box-sc-g0xbh4-0 jahcnb"><span role="tooltip" aria-label="Add file" class="Tooltip__TooltipBase-sc-uha8qm-0 iSGYLp tooltipped-s"><a sx="[object Object]" data-component="IconButton" type="button" aria-label="Add file" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 eCoUah" href="/twisted/twisted/new/trunk"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-plus" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg></a></span><button data-component="IconButton" type="button" aria-label="Search this repository" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 cIsLoD"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button></div></div></div><div class="Box-sc-g0xbh4-0 ccToMy"><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button><span class="TextInputWrapper__TextInputBaseWrapper-sc-1mqhpbi-0 TextInputWrapper-sc-1mqhpbi-1 iOFiIT fvMdhy TextInput-wrapper" aria-busy="false"><span class="TextInput-icon"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></span><input type="text" aria-label="Go to file" role="combobox" aria-controls="file-results-list" aria-expanded="false" aria-haspopup="dialog" autoCorrect="off" spellcheck="false" placeholder="Go to file" data-component="input" class="UnstyledTextInput-sc-14ypya-0 cDLBls" value=""/><span class="TextInput-icon"><div class="Box-sc-g0xbh4-0 cNvKlH"><kbd>t</kbd></div></span></span></div><div class="Box-sc-g0xbh4-0 cLfAnm"><div class="react-tree-show-tree-items"><div data-testid="repos-file-tree-container" class="Box-sc-g0xbh4-0 erWCJP"><nav aria-label="File Tree Navigation"><span role="status" aria-live="polite" aria-atomic="true" class="_VisuallyHidden__VisuallyHidden-sc-11jhm7a-0 rTZSs"></span><ul role="tree" aria-label="Files" class="TreeView__UlBox-sc-4ex6b6-0 dDkgrC"><li class="PRIVATE_TreeView-item" tabindex="0" id=".github-item" role="treeitem" aria-labelledby=":Rqcndjal5:" aria-describedby=":Rqcndjal5H1: :Rqcndjal5H2:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":Rqcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":Rqcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text"><span>.github</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="admin-item" role="treeitem" aria-labelledby=":R1acndjal5:" aria-describedby=":R1acndjal5H1: :R1acndjal5H2:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":R1acndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R1acndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text"><span>admin</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="bin-item" role="treeitem" aria-labelledby=":R1qcndjal5:" aria-describedby=":R1qcndjal5H1: :R1qcndjal5H2:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":R1qcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R1qcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text"><span>bin</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="docs-item" role="treeitem" aria-labelledby=":R2acndjal5:" aria-describedby=":R2acndjal5H1: :R2acndjal5H2:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":R2acndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R2acndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text"><span>docs</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="src-item" role="treeitem" aria-labelledby=":R2qcndjal5:" aria-describedby=":R2qcndjal5H1: :R2qcndjal5H2:" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id=":R2qcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R2qcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text"><span>src</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id=".coveragerc-item" role="treeitem" aria-labelledby=":R3acndjal5:" aria-describedby=":R3acndjal5H1: :R3acndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R3acndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R3acndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>.coveragerc</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id=".git-blame-ignore-revs-item" role="treeitem" aria-labelledby=":R3qcndjal5:" aria-describedby=":R3qcndjal5H1: :R3qcndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R3qcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R3qcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>.git-blame-ignore-revs</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id=".gitattributes-item" role="treeitem" aria-labelledby=":R4acndjal5:" aria-describedby=":R4acndjal5H1: :R4acndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R4acndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R4acndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>.gitattributes</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id=".gitignore-item" role="treeitem" aria-labelledby=":R4qcndjal5:" aria-describedby=":R4qcndjal5H1: :R4qcndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R4qcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R4qcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>.gitignore</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id=".pre-commit-config.yaml-item" role="treeitem" aria-labelledby=":R5acndjal5:" aria-describedby=":R5acndjal5H1: :R5acndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R5acndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R5acndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>.pre-commit-config.yaml</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id=".readthedocs.yml-item" role="treeitem" aria-labelledby=":R5qcndjal5:" aria-describedby=":R5qcndjal5H1: :R5qcndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R5qcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R5qcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>.readthedocs.yml</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="CONTRIBUTING.md-item" role="treeitem" aria-labelledby=":R6acndjal5:" aria-describedby=":R6acndjal5H1: :R6acndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R6acndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R6acndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>CONTRIBUTING.md</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="INSTALL.rst-item" role="treeitem" aria-labelledby=":R6qcndjal5:" aria-describedby=":R6qcndjal5H1: :R6qcndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R6qcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R6qcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>INSTALL.rst</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="LICENSE-item" role="treeitem" aria-labelledby=":R7acndjal5:" aria-describedby=":R7acndjal5H1: :R7acndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R7acndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R7acndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>LICENSE</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="NEWS.rst-item" role="treeitem" aria-labelledby=":R7qcndjal5:" aria-describedby=":R7qcndjal5H1: :R7qcndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R7qcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R7qcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>NEWS.rst</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="README.rst-item" role="treeitem" aria-labelledby=":R8acndjal5:" aria-describedby=":R8acndjal5H1: :R8acndjal5H2:" aria-level="1" aria-current="true" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R8acndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R8acndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>README.rst</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="code_of_conduct.md-item" role="treeitem" aria-labelledby=":R8qcndjal5:" aria-describedby=":R8qcndjal5H1: :R8qcndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R8qcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R8qcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>code_of_conduct.md</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="codecov.yml-item" role="treeitem" aria-labelledby=":R9acndjal5:" aria-describedby=":R9acndjal5H1: :R9acndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R9acndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R9acndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>codecov.yml</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="hatch_build.py-item" role="treeitem" aria-labelledby=":R9qcndjal5:" aria-describedby=":R9qcndjal5H1: :R9qcndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":R9qcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":R9qcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>hatch_build.py</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="pyproject.toml-item" role="treeitem" aria-labelledby=":Raacndjal5:" aria-describedby=":Raacndjal5H1: :Raacndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Raacndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":Raacndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>pyproject.toml</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="setup.cfg-item" role="treeitem" aria-labelledby=":Raqcndjal5:" aria-describedby=":Raqcndjal5H1: :Raqcndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Raqcndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":Raqcndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>setup.cfg</span></span></div></div></li><li class="PRIVATE_TreeView-item" tabindex="0" id="tox.ini-item" role="treeitem" aria-labelledby=":Rbacndjal5:" aria-describedby=":Rbacndjal5H1: :Rbacndjal5H2:" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container" style="--level:1;content-visibility:auto;contain-intrinsic-size:auto 2rem"><div style="grid-area:spacer;display:flex"><div style="width:100%;display:flex"></div></div><div id=":Rbacndjal5:" class="PRIVATE_TreeView-item-content"><div class="PRIVATE_VisuallyHidden" aria-hidden="true" id=":Rbacndjal5H1:"></div><div class="PRIVATE_TreeView-item-visual" aria-hidden="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text"><span>tox.ini</span></span></div></div></li></ul></nav></div></div><div class="Box-sc-g0xbh4-0 hwhShM"><div class="Box-sc-g0xbh4-0 cYPxpP"><a href="https://docs.github.com/repositories/working-with-files/using-files/navigating-code-on-github" target="_blank" class="Link__StyledLink-sc-14289xe-0 gPmdpC">Documentation</a> • <a href="https://github.com/orgs/community/discussions/54546" target="_blank" class="Link__StyledLink-sc-14289xe-0 gPmdpC">Share feedback</a></div></div></div><div class="Box-sc-g0xbh4-0 fBtiVT"><div class="Box-sc-g0xbh4-0 cYPxpP"><a href="https://docs.github.com/repositories/working-with-files/using-files/navigating-code-on-github" target="_blank" class="Link__StyledLink-sc-14289xe-0 gPmdpC">Documentation</a> • <a href="https://github.com/orgs/community/discussions/54546" target="_blank" class="Link__StyledLink-sc-14289xe-0 gPmdpC">Share feedback</a></div></div></div></div></div></div></div><main class="Box-sc-g0xbh4-0 emFMJu"><div class="Box-sc-g0xbh4-0"></div><div class="Box-sc-g0xbh4-0 hlUAHL"><div data-selector="repos-split-pane-content" tabindex="0" class="Box-sc-g0xbh4-0 iStsmI"><div class="Box-sc-g0xbh4-0 eIgvIk"><div class="Box-sc-g0xbh4-0 eVFfWF container"><div class="Box-sc-g0xbh4-0 kgXdnT react-code-view-header--narrow"><div class="Box-sc-g0xbh4-0 kzTa-dF"><div class="Box-sc-g0xbh4-0 bbXCl"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 fNPcqd"><button style="--button-color:fg.muted" type="button" aria-label="Expand side panel" data-testid="expand-file-tree-button-mobile" class="types__StyledButton-sc-ws60qy-0 bWtVmw"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-arrow-left" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M7.78 12.53a.75.75 0 0 1-1.06 0L2.47 8.28a.75.75 0 0 1 0-1.06l4.25-4.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L4.81 7h7.44a.75.75 0 0 1 0 1.5H4.81l2.97 2.97a.75.75 0 0 1 0 1.06Z"></path></svg></span><span data-component="text">Files</span></span></button><button data-component="IconButton" type="button" data-testid="collapse-file-tree-button" aria-label="Side panel" aria-expanded="true" aria-controls="repos-file-tree" class="types__StyledButton-sc-ws60qy-0 imyHbr" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-sidebar-expand" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.177 7.823 2.396-2.396A.25.25 0 0 1 7 5.604v4.792a.25.25 0 0 1-.427.177L4.177 8.177a.25.25 0 0 1 0-.354Z"></path><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25H9.5v-13Zm12.5 13a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11v13Z"></path></svg></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button></h2><div class="Box-sc-g0xbh4-0 hGGMNu"><div class="Box-sc-g0xbh4-0 eHRrYV"><button type="button" id="branch-picker-repos-header-ref-selector-narrow" aria-haspopup="true" tabindex="0" aria-label="trunk branch" data-testid="anchor-button" class="types__StyledButton-sc-ws60qy-0 jyKsKT ref-selector-class"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text"><div class="Box-sc-g0xbh4-0 bKgizp"><div class="Box-sc-g0xbh4-0 fxhqJs"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="Box-sc-g0xbh4-0 dKmYfk"><span class="Text-sc-17v1xeu-0 bOMzPg"> <!-- -->trunk</span></div></div></span><span data-component="trailingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><button hidden="" data-hotkey-scope="read-only-cursor-text-area"></button></div> <button type="button" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 btfozg"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text">Blame</span></span></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button data-component="IconButton" type="button" aria-label="More file actions" class="types__StyledButton-sc-ws60qy-0 iflFHp js-blob-dropdown-click" title="More file actions" data-testid="more-file-actions-button" id=":R9aaqjal5:" aria-haspopup="true" tabindex="0" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button> </div></div><div class="Box-sc-g0xbh4-0 hSNzKh"><div class="Box-sc-g0xbh4-0 eTvGbF"><nav data-testid="breadcrumbs" aria-labelledby="repos-header-breadcrumb-mobile-heading" id="repos-header-breadcrumb-mobile" class="Box-sc-g0xbh4-0 kzRgrI"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading" id="repos-header-breadcrumb-mobile-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 cmAPIB"><li class="Box-sc-g0xbh4-0 jwXCBK"><a sx="[object Object]" data-testid="breadcrumbs-repo-link" class="Link__StyledLink-sc-14289xe-0 bQnDDD" href="/twisted/twisted/tree/trunk">twisted</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 jwXCBK"><span aria-hidden="true" class="Text-sc-17v1xeu-0 kvpHZx">/</span><h1 tabindex="-1" id="file-name-id-mobile" class="Heading__StyledHeading-sc-1c1dgg0-0 diwsLq">README.rst</h1></div><button data-component="IconButton" type="button" aria-label="Copy path" data-testid="breadcrumb-copy-path-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 degAHJ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button></div></div></div></div><div id="StickyHeader" class="Box-sc-g0xbh4-0 bDwCYs react-code-view-header--wide"><div class="Box-sc-g0xbh4-0 fywjmm"><div class="Box-sc-g0xbh4-0 dyczTK"><div class="Box-sc-g0xbh4-0 kszRgZ"><div class="Box-sc-g0xbh4-0 eTvGbF"><nav data-testid="breadcrumbs" aria-labelledby="repos-header-breadcrumb-wide-heading" id="repos-header-breadcrumb-wide" class="Box-sc-g0xbh4-0 kzRgrI"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading" id="repos-header-breadcrumb-wide-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 cmAPIB"><li class="Box-sc-g0xbh4-0 jwXCBK"><a sx="[object Object]" data-testid="breadcrumbs-repo-link" class="Link__StyledLink-sc-14289xe-0 bQnDDD" href="/twisted/twisted/tree/trunk">twisted</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 jwXCBK"><span aria-hidden="true" class="Text-sc-17v1xeu-0 kvpHZx">/</span><h1 tabindex="-1" id="file-name-id-wide" class="Heading__StyledHeading-sc-1c1dgg0-0 diwsLq">README.rst</h1></div><button data-component="IconButton" type="button" aria-label="Copy path" data-testid="breadcrumb-copy-path-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 degAHJ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button></div></div><div class="Box-sc-g0xbh4-0 gtBUEp"><div class="d-flex gap-2"> <button type="button" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 btfozg"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text">Blame</span></span></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button data-component="IconButton" type="button" aria-label="More file actions" class="types__StyledButton-sc-ws60qy-0 iflFHp js-blob-dropdown-click" title="More file actions" data-testid="more-file-actions-button" id=":R9pkqjal5:" aria-haspopup="true" tabindex="0" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button> </div></div></div></div></div></div></div><div class="Box-sc-g0xbh4-0 MERGN react-code-view-bottom-padding"> <div class="Box-sc-g0xbh4-0 cMYnca"></div><div class="Box-sc-g0xbh4-0"></div> <!-- --> <!-- --> </div><div class="Box-sc-g0xbh4-0 MERGN"> <!-- --> <!-- --> <div class="Box-sc-g0xbh4-0 dfEVSV"><div class="Box-sc-g0xbh4-0 eYedVD"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading">Latest commit</h2><div style="width:120px" class="Skeleton Skeleton--text" data-testid="loading"> </div><div class="Box-sc-g0xbh4-0 jGfYmh"><div data-testid="latest-commit-details" class="Box-sc-g0xbh4-0 lhFvfi"></div><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading">History</h2><a aria-label="Commit history" class="types__StyledButton-sc-ws60qy-0 fUlRWz react-last-commit-history-group" href="/twisted/twisted/commits/trunk/README.rst" data-size="small"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span><span data-component="text"><span class="Text-sc-17v1xeu-0 djgCKN">History</span></span></span></a><div class="Box-sc-g0xbh4-0 bqgLjk"></div><span role="tooltip" aria-label="Commit history" class="Tooltip__TooltipBase-sc-uha8qm-0 iSGYLp tooltipped-n"><a aria-label="Commit history" class="types__StyledButton-sc-ws60qy-0 fUlRWz react-last-commit-history-icon" href="/twisted/twisted/commits/trunk/README.rst"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span></span></a></span></div></div></div><div class="Box-sc-g0xbh4-0 iJmJly"><div class="Box-sc-g0xbh4-0 jACbi container"><div class="Box-sc-g0xbh4-0 bSdwWB react-code-size-details-banner"><div class="Box-sc-g0xbh4-0 fleZSW react-code-size-details-banner"><div class="Box-sc-g0xbh4-0 jALzIY text-mono"><div title="4.42 KB" data-testid="blob-size" class="Truncate__StyledTruncate-sc-23o1d2-0 fUpWeN"><span class="Text-sc-17v1xeu-0 gPDEWA">123 lines (77 loc) · 4.42 KB</span></div></div></div></div><div class="Box-sc-g0xbh4-0 gBKNLX react-blob-view-header-sticky" id="repos-sticky-header"><div class="Box-sc-g0xbh4-0 ePiodO"><div class="Box-sc-g0xbh4-0 react-blob-sticky-header"><div class="Box-sc-g0xbh4-0 kQJlnf"><div class="Box-sc-g0xbh4-0 gJICKO"><div class="Box-sc-g0xbh4-0 iZJewz"><nav data-testid="breadcrumbs" aria-labelledby="sticky-breadcrumb-heading" id="sticky-breadcrumb" class="Box-sc-g0xbh4-0 kzRgrI"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading" id="sticky-breadcrumb-heading">Breadcrumbs</h2><ol class="Box-sc-g0xbh4-0 cmAPIB"><li class="Box-sc-g0xbh4-0 jwXCBK"><a sx="[object Object]" data-testid="breadcrumbs-repo-link" class="Link__StyledLink-sc-14289xe-0 bQnDDD" href="/twisted/twisted/tree/trunk">twisted</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Box-sc-g0xbh4-0 jwXCBK"><span aria-hidden="true" class="Text-sc-17v1xeu-0 kpJgoj">/</span><h1 tabindex="-1" id="sticky-file-name-id" class="Heading__StyledHeading-sc-1c1dgg0-0 jAEDJk">README.rst</h1></div></div><button style="--button-color:fg.default" type="button" data-size="small" class="types__StyledButton-sc-ws60qy-0 hhwrXY"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="leadingVisual" class="Box-sc-g0xbh4-0 trpoQ"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-arrow-up" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M3.47 7.78a.75.75 0 0 1 0-1.06l4.25-4.25a.75.75 0 0 1 1.06 0l4.25 4.25a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018L9 4.81v7.44a.75.75 0 0 1-1.5 0V4.81L4.53 7.78a.75.75 0 0 1-1.06 0Z"></path></svg></span><span data-component="text">Top</span></span></button></div></div></div><div class="Box-sc-g0xbh4-0 jgMUtU"><h2 class="Heading__StyledHeading-sc-1c1dgg0-0 cgQnMS sr-only" data-testid="screen-reader-heading">File metadata and controls</h2><div class="Box-sc-g0xbh4-0 bfkNRF"><ul aria-label="File view" class="SegmentedControl__SegmentedControlList-sc-1rzig82-0 hDkNhA"><li class="Box-sc-g0xbh4-0 fXBLEV"><button aria-current="true" class="SegmentedControlButton__SegmentedControlButtonStyled-sc-8lkgxl-0 kcTGcx"><span class="segmentedControl-content"><div class="Box-sc-g0xbh4-0 segmentedControl-text">Preview</div></span></button></li><li class="Box-sc-g0xbh4-0 eejbCg"><button aria-current="false" class="SegmentedControlButton__SegmentedControlButtonStyled-sc-8lkgxl-0 WHXNM"><span class="segmentedControl-content"><div class="Box-sc-g0xbh4-0 segmentedControl-text">Code</div></span></button></li><li class="Box-sc-g0xbh4-0 eejbCg"><button aria-current="false" class="SegmentedControlButton__SegmentedControlButtonStyled-sc-8lkgxl-0 iQDmCy"><span class="segmentedControl-content"><div class="Box-sc-g0xbh4-0 segmentedControl-text">Blame</div></span></button></li></ul><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><div class="Box-sc-g0xbh4-0 fleZSW react-code-size-details-in-header"><div class="Box-sc-g0xbh4-0 jALzIY text-mono"><div title="4.42 KB" data-testid="blob-size" class="Truncate__StyledTruncate-sc-23o1d2-0 fUpWeN"><span class="Text-sc-17v1xeu-0 gPDEWA">123 lines (77 loc) · 4.42 KB</span></div></div></div></div><div class="Box-sc-g0xbh4-0 iBylDf"><div class="Box-sc-g0xbh4-0 kSGBPx react-blob-header-edit-and-raw-actions"><div class="ButtonGroup-sc-1gxhls1-0 cjbBGq"><a href="https://github.com/twisted/twisted/raw/trunk/README.rst" data-testid="raw-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 fRleic"><span data-component="buttonContent" class="Box-sc-g0xbh4-0 kkrdEu"><span data-component="text">Raw</span></span></a><button data-component="IconButton" type="button" aria-label="Copy raw content" data-testid="copy-raw-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 iclSHR"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button><span role="tooltip" aria-label="Download raw file" class="Tooltip__TooltipBase-sc-uha8qm-0 iSGYLp tooltipped-n"><button data-component="IconButton" type="button" aria-label="Download raw content" data-testid="download-raw-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 bykEZB"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-download" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M2.75 14A1.75 1.75 0 0 1 1 12.25v-2.5a.75.75 0 0 1 1.5 0v2.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 14Z"></path><path d="M7.25 7.689V2a.75.75 0 0 1 1.5 0v5.689l1.97-1.969a.749.749 0 1 1 1.06 1.06l-3.25 3.25a.749.749 0 0 1-1.06 0L4.22 6.78a.749.749 0 1 1 1.06-1.06l1.97 1.969Z"></path></svg></button></span></div><button hidden="" data-testid="raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="copy-raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="download-raw-button-shortcut" data-hotkey-scope="read-only-cursor-text-area"></button><a class="Link__StyledLink-sc-14289xe-0 gPmdpC js-github-dev-shortcut d-none" href="https://github.dev/"></a><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><a class="Link__StyledLink-sc-14289xe-0 gPmdpC js-github-dev-new-tab-shortcut d-none" href="https://github.dev/" target="_blank"></a><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><div class="ButtonGroup-sc-1gxhls1-0 cjbBGq"><span role="tooltip" aria-label="Fork this repository and edit the file" class="Tooltip__TooltipBase-sc-uha8qm-0 iSGYLp tooltipped-nw"><a sx="[object Object]" data-component="IconButton" type="button" aria-label="Edit file" data-testid="edit-button" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 iEfBoP" href="/twisted/twisted/edit/trunk/README.rst"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-pencil" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg></a></span><button data-component="IconButton" type="button" aria-label="More edit options" data-testid="more-edit-button" id=":Rl7pjqlajal5:" aria-haspopup="true" tabindex="0" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 iclSHR"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></button></div><button hidden="" data-testid="" data-hotkey="e,E" data-hotkey-scope="read-only-cursor-text-area"></button></div><button data-component="IconButton" type="button" aria-label="Outline" aria-pressed="false" data-size="small" data-no-visuals="true" class="types__StyledButton-sc-ws60qy-0 iajnCX"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-list-unordered" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M5.75 2.5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5ZM2 14a1 1 0 1 1 0-2 1 1 0 0 1 0 2Zm1-6a1 1 0 1 1-2 0 1 1 0 0 1 2 0ZM2 4a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path></svg></button><div class="Box-sc-g0xbh4-0 react-blob-header-edit-and-raw-actions-combined"><button data-component="IconButton" type="button" aria-label="Edit and raw actions" class="types__StyledButton-sc-ws60qy-0 grSsTo js-blob-dropdown-click" title="More file actions" data-testid="more-file-actions-button" id=":R1dpjqlajal5:" aria-haspopup="true" tabindex="0" data-size="small" data-no-visuals="true"><svg aria-hidden="true" focusable="false" role="img" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" style="display:inline-block;user-select:none;vertical-align:text-bottom;overflow:visible"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button></div></div></div></div><div class="Box-sc-g0xbh4-0"></div></div><div class="Box-sc-g0xbh4-0 dWbgpS"><section aria-labelledby="file-name-id-wide file-name-id-mobile" class="Box-sc-g0xbh4-0 eRvpKx"><div class="Box-sc-g0xbh4-0 cTsUqU js-snippet-clipboard-copy-unpositioned" data-hpc="true"><article class="markdown-body entry-content container-lg" itemprop="text"><h1 tabindex="-1" id="user-content-twisted" dir="auto"><a class="heading-link" href="#twisted">Twisted<svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></h1>
<p dir="auto"><a href="https://gitter.im/twisted/twisted" rel="nofollow"><img alt="gitter" src="https://camo.githubusercontent.com/36f12e64939abe7eaaf00e9e2377940ea0b4405b12ca5dcc1431635dd2febee1/68747470733a2f2f696d672e736869656c64732e696f2f6769747465722f726f6f6d2f747769737465642f747769737465642e737667" data-canonical-src="https://img.shields.io/gitter/room/twisted/twisted.svg" style="max-width: 100%;">
</a>
<a href="https://docs.twistedmatrix.com" rel="nofollow"><img alt="rtd" src="https://camo.githubusercontent.com/0737bc1c19c49f509d4db9e23476bf3f9a0567f602672138b7aeff8002a53bdb/68747470733a2f2f72656164746865646f63732e6f72672f70726f6a656374732f747769737465642f62616467652f3f76657273696f6e3d6c6174657374267374796c653d666c6174" data-canonical-src="https://readthedocs.org/projects/twisted/badge/?version=latest&amp;style=flat" style="max-width: 100%;"></a>
<a href="https://pypi.python.org/pypi/twisted" rel="nofollow"><img alt="pypi" src="https://camo.githubusercontent.com/ab2e87784e4c40ac138408a6d5d6c39351694fc517b4da12649cb4acd882bcde/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f747769737465642e737667" data-canonical-src="https://img.shields.io/pypi/v/twisted.svg" style="max-width: 100%;">
</a>
<a href="https://github.com/twisted/twisted"><img alt="ci" src="https://github.com/twisted/twisted/actions/workflows/test.yaml/badge.svg" style="max-width: 100%;">
</a></p>
<p dir="auto">For information on changes in this release, see the <a href="/twisted/twisted/blob/trunk/NEWS.rst">NEWS</a> file.</p>
<a name="user-content-what-is-this"></a>
<h2 tabindex="-1" id="user-content-what-is-this" dir="auto"><a class="heading-link" href="#what-is-this">What is this?<svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></h2>
<p dir="auto">Twisted is an event-based framework for internet applications, supporting Python 3.6+.
It includes modules for many different purposes, including the following:</p>
<ul dir="auto">
<li><code>twisted.web</code>: HTTP clients and servers, HTML templating, and a WSGI server</li>
<li><code>twisted.conch</code>: SSHv2 and Telnet clients and servers and terminal emulators</li>
<li><code>twisted.words</code>: Clients and servers for IRC, XMPP, and other IM protocols</li>
<li><code>twisted.mail</code>: IMAPv4, POP3, SMTP clients and servers</li>
<li><code>twisted.positioning</code>: Tools for communicating with NMEA-compatible GPS receivers</li>
<li><code>twisted.names</code>: DNS client and tools for making your own DNS servers</li>
<li><code>twisted.trial</code>: A unit testing framework that integrates well with Twisted-based code.</li>
</ul>
<p dir="auto">Twisted supports all major system event loops -- <code>select</code> (all platforms), <code>poll</code> (most POSIX platforms), <code>epoll</code> (Linux), <code>kqueue</code> (FreeBSD, macOS), IOCP (Windows), and various GUI event loops (GTK+2/3, Qt, wxWidgets).
Third-party reactors can plug into Twisted, and provide support for additional event loops.</p>
<a name="user-content-installing"></a>
<h2 tabindex="-1" id="user-content-installing" dir="auto"><a class="heading-link" href="#installing">Installing<svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></h2>
<p dir="auto">To install the latest version of Twisted using pip:</p>
<pre>$ pip install twisted
</pre>
<p dir="auto">Additional instructions for installing this software are in <a href="/twisted/twisted/blob/trunk/INSTALL.rst">the installation instructions</a>.</p>
<a name="user-content-documentation-and-support"></a>
<h2 tabindex="-1" id="user-content-documentation-and-support" dir="auto"><a class="heading-link" href="#documentation-and-support">Documentation and Support<svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></h2>
<p dir="auto">Twisted's documentation is available from the <a href="https://twistedmatrix.com/documents/current/" rel="nofollow">Twisted Matrix website</a>.
This documentation contains how-tos, code examples, and an API reference.</p>
<p dir="auto">Help is also available on the <a href="https://mail.python.org/mailman3/lists/twisted.python.org/" rel="nofollow">Twisted mailing list</a>.</p>
<p dir="auto">There is also an IRC channel, <code>#twisted</code>,
on the <a href="https://libera.chat/" rel="nofollow">Libera.Chat</a> network.
A web client is available at <a href="https://web.libera.chat/" rel="nofollow">web.libera.chat</a>.</p>
<a name="user-content-unit-tests"></a>
<h2 tabindex="-1" id="user-content-unit-tests" dir="auto"><a class="heading-link" href="#unit-tests">Unit Tests<svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></h2>
<p dir="auto">Twisted has a comprehensive test suite, which can be run by <code>tox</code>:</p>
<pre>$ tox -l                       # to view all test environments
$ tox -e nocov                 # to run all the tests without coverage
$ tox -e withcov               # to run all the tests with coverage
$ tox -e alldeps-withcov-posix # install all dependencies, run tests with coverage on POSIX platform
</pre>
<p dir="auto">You can test running the test suite under the different reactors with the <code>TWISTED_REACTOR</code> environment variable:</p>
<pre>$ env TWISTED_REACTOR=epoll tox -e alldeps-withcov-posix
</pre>
<p dir="auto">Some of these tests may fail if you:</p>
<ul dir="auto">
<li>don't have the dependencies required for a particular subsystem installed,</li>
<li>have a firewall blocking some ports (or things like Multicast, which Linux NAT has shown itself to do), or</li>
<li>run them as root.</li>
</ul>
<a name="user-content-static-code-checkers"></a>
<h2 tabindex="-1" id="user-content-static-code-checkers" dir="auto"><a class="heading-link" href="#static-code-checkers">Static Code Checkers<svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></h2>
<p dir="auto">You can ensure that code complies to Twisted <a href="https://twistedmatrix.com/documents/current/core/development/policy/coding-standard.html" rel="nofollow">coding standards</a>:</p>
<pre>$ tox -e lint   # run pre-commit to check coding stanards
$ tox -e mypy   # run MyPy static type checker to check for type errors
</pre>
<p dir="auto">Or, for speed, use pre-commit directly:</p>
<pre>$ pipx run pre-commit run
</pre>
<a name="user-content-copyright"></a>
<h2 tabindex="-1" id="user-content-copyright" dir="auto"><a class="heading-link" href="#copyright">Copyright<svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></h2>
<p dir="auto">All of the code in this distribution is Copyright (c) 2001-2023 Twisted Matrix Laboratories.</p>
<p dir="auto">Twisted is made available under the MIT license.
The included <a href="/twisted/twisted/blob/trunk/LICENSE">LICENSE</a> file describes this in detail.</p>
<a name="user-content-warranty"></a>
<h2 tabindex="-1" id="user-content-warranty" dir="auto"><a class="heading-link" href="#warranty">Warranty<svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></h2>
<blockquote>
<p dir="auto">THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER
EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS
TO THE USE OF THIS SOFTWARE IS WITH YOU.</p>
<p dir="auto">IN NO EVENT WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY
AND/OR REDISTRIBUTE THE LIBRARY, BE LIABLE TO YOU FOR ANY DAMAGES, EVEN IF
SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH
DAMAGES.</p>
</blockquote>
<p dir="auto">Again, see the included <a href="/twisted/twisted/blob/trunk/LICENSE">LICENSE</a> file for specific legal details.</p>

</article></div><button hidden=""></button></section></div></div></div> <!-- --> <!-- --> </div></div></div><div class="Box-sc-g0xbh4-0"></div></main></div></div></div><div id="find-result-marks-container" class="Box-sc-g0xbh4-0 aZrVR"></div><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden=""></button></div> <!-- --> <!-- --> <!-- --> <script type="application/json" id="__PRIMER_DATA__">{"resolvedServerColorMode":"night"}</script></div>
</react-app>
</turbo-frame>



  </div>

</turbo-frame>

    </main>
  </div>

  </div>

          <footer class="footer width-full container-xl p-responsive" role="contentinfo">
  <h2 class='sr-only'>Footer</h2>

  <div class="position-relative d-flex flex-items-center pb-2 f6 color-fg-muted border-top color-border-muted flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap mt-6 pt-6">
    <div class="list-style-none d-flex flex-wrap col-0 col-lg-2 flex-justify-start flex-lg-justify-between mb-2 mb-lg-0">
      <div class="mt-2 mt-lg-0 d-flex flex-items-center">
        <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-2" href="https://github.com">
          <svg aria-hidden="true" height="24" viewBox="0 0 16 16" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
</a>        <span>
        &copy; 2023 GitHub, Inc.
        </span>
      </div>
    </div>

    <nav aria-label='Footer' class="col-12 col-lg-8">
      <h3 class='sr-only' id='sr-footer-heading'>Footer navigation</h3>
      <ul class="list-style-none d-flex flex-wrap col-12 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0" aria-labelledby='sr-footer-heading'>
          <li class="mr-3 mr-lg-0"><a href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}">Terms</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}">Privacy</a></li>
          <li class="mr-3 mr-lg-0"><a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security">Security</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://www.githubstatus.com/" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}">Status</a></li>
          <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to help, text:Docs" href="https://docs.github.com">Docs</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://support.github.com?tags=dotcom-footer" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}">Contact GitHub</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://github.com/pricing" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Pricing&quot;,&quot;label&quot;:&quot;text:Pricing&quot;}">Pricing</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://docs.github.com" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to api&quot;,&quot;label&quot;:&quot;text:api&quot;}">API</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://services.github.com" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to training&quot;,&quot;label&quot;:&quot;text:training&quot;}">Training</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://github.blog" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to blog&quot;,&quot;label&quot;:&quot;text:blog&quot;}">Blog</a></li>
          <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>
      </ul>
    </nav>
  </div>

  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 color-fg-muted"></span>
  </div>
</footer>




  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden>
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

    <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default color-fg-default hx_rsm" open>
    <summary role="button" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast hx_rsm-dialog hx_rsm-modal">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;">
  </div>
</div>

    <template id="snippet-clipboard-copy-button">
  <div class="zeroclipboard-container position-absolute right-0 top-0">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0 tooltipped-no-delay" data-copy-feedback="Copied!" data-tooltip-direction="w">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none m-2">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div>
</template>
<template id="snippet-clipboard-copy-button-unpositioned">
  <div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div>
</template>


    <style>
      .user-mention[href$="/AleksNeStu"] {
        color: var(--color-user-mention-fg);
        background-color: var(--color-user-mention-bg);
        border-radius: 2px;
        margin-left: -2px;
        margin-right: -2px;
        padding: 0 2px;
      }
    </style>


    </div>

    <div id="js-global-screen-reader-notice" class="sr-only" aria-live="polite" ></div>
  </body>
</html>


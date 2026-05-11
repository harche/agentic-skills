# Product Life Cycle API Reference

## Endpoint

```
GET https://access.redhat.com/product-life-cycles/api/v1/products?name=<substring>
```

No authentication required. The `name` parameter is a case-insensitive substring match.

## Product Object

| Field | Type | Description |
|---|---|---|
| `name` | string | Current product name |
| `former_names` | string[] | Previous product names (useful for search fallback) |
| `is_operator` | bool | Whether this product is an OLM-managed operator |
| `is_layered_product` | bool | Whether this product is layered on OpenShift |
| `is_retired` | bool | Whether the entire product has been retired |
| `package` | string\|null | **OLM package name** — maps to Subscription `spec.name` |
| `versions` | object[] | Per-version lifecycle data |

### The `package` field

The `package` field is the OLM package name and provides an **exact match key** to correlate
Product Life Cycle products with OLM Subscriptions. This is more reliable than name matching.

Mapping: `product.package` == `subscription.spec.name`

## Version Object

| Field | Type | Description |
|---|---|---|
| `name` | string | Version number (e.g., `"6.5"`, `"4.21"`) |
| `type` | string | **Current support status** — see table below |
| `openshift_compatibility` | string\|null | Comma-separated OCP versions (e.g., `"4.19, 4.20, 4.21"`) — only on layered products |
| `phases` | object[] | Lifecycle phase details with dates |

### Support status (`type`)

| Value | Meaning |
|---|---|
| `"Full Support"` | Active development, bug fixes, security patches |
| `"Maintenance Support"` | Critical/security fixes only, no new features |
| `"End of Maintenance"` | Maintenance support has ended; no EUS/ELS applies to this version |
| `"Extended Support"` | Past maintenance, currently in a paid Extended Life Cycle Support (ELS) phase |
| `"End of life"` | No fixes, no support — must upgrade |
| `""` (empty) | Status not yet determined (e.g., version has incomplete lifecycle data) |

## Phase Object

| Field | Type | Description |
|---|---|---|
| `name` | string | Phase name (e.g., `"General availability"`, `"Full support"`, `"Maintenance support"`) |
| `start_date` | string | Phase start — ISO 8601 date or descriptive string |
| `end_date` | string | Phase end — ISO 8601 date or descriptive string |
| `date_format` | string | `"date"` (ISO 8601) or `"string"` (relative/TBD) |

Phase names vary by product. Common categories:

| Category | Phase names | Meaning |
|---|---|---|
| Release | `General availability` | When the version was first released |
| Active support | `Full support` | Active development, bug fixes, security patches |
| Reduced support | `Maintenance support`, `Maintenance Support 1`, `Maintenance support 2` | Critical/security fixes only |
| Extended support | `Extended update support`, `Extended update support Term 2`, `Extended update support Term 3` | EUS — available for select versions, may require add-on purchase |
| Extended lifecycle | `Extended life phase`, `Extended life cycle support (ELS) 1`/`2`, `Extended life cycle support (ELS) add-on`/`Term 2 add-on`/`Term 3 add-on` | Paid extended support beyond normal EOL |
| End | `End of Life`, `Retired` | No further updates or support |
| Other | `Migration support`, `Third-party certification period` | Product-specific transitional phases |

Phase names are not standardized across products. Use the `start_date` and `end_date` fields
to determine whether a phase is current, rather than relying on the phase name alone.

For detailed lifecycle policy definitions, see the [Red Hat product lifecycle policies](https://access.redhat.com/support/policy/updates/openshift#dates).

## Search Tips

1. **Be specific with `?name=`** — `"logging+for+Red+Hat+OpenShift"` is better than `"logging"`
2. **Check `former_names`** — products may appear under a previous name in the `former_names` field
3. **Use `is_operator: true`** to filter for OLM operators in results
4. **Use `package` for OLM correlation** — more reliable than name matching
5. **Never omit `?name=`** — the unfiltered response is very large

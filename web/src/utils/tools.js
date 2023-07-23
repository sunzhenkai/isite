/* 工具类 */
import $script from 'scriptjs'

export function concatDict (dicts) {
  let res = {}

  if (dicts && dicts.constructor.name === 'Array') {
    dicts.forEach(function (dict) {
      if (dict) {
        for (k in dict) {
          if (dict.hasOwnProperty(k)) {
            res[k] = dict[k]
          }
        }
      }
    })
  }

  return res
}

export function formatDate (dt) {
  let day = dt.getDate();
  let monthIndex = dt.getMonth();
  let year = dt.getFullYear();
  let hour = dt.getHours();
  let minute = dt.getMinutes();
  let second = dt.getSeconds();

  return year + '-' + (monthIndex+1) + '-' + day + ' ' + hour + ':' + minute + ':' + second;
}

export function fetchScript (url) {
  return new Promise((resolve) => {
    $script(url, () => {
      resolve();
    })
  })
}
